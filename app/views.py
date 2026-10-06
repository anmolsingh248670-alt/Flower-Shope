from django.shortcuts import render,redirect
from .models import add_product,Cart,Adders,Review,OrderItem
from .forms import add_projuct_Forms
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
import random
from django.core.mail import send_mail

# Create your views here.
def home(request):

    data = add_product.objects.all()

    cart_items = Cart.objects.none()
    cart_quantity = 0
    total = 0
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        for item in cart_items:
            cart_quantity += item.quantity
            total += item.quantity * item.Product.final_price
    context = {
        'data': data,
        'cart_items': cart_items,
        'total': total,
        'cart_quantity': cart_quantity,
    }
    return render(request, 'home.html', context)
# by products Page 
@login_required(login_url='home_login')
# from django.shortcuts import render
# from .models import add_product, Cart

def by_products(request):

    data = add_product.objects.all()

    cart_items = Cart.objects.filter(
        user=request.user
    )
    cart_quantity = 0

    for item in cart_items:
     cart_quantity += item.quantity

    total = 0

    for item in cart_items:
        total += item.quantity * item.Product.final_price

    context = {
        'data': data,
        'cart_items': cart_items,
        'total': total,
        'cart_quantity': cart_quantity,
    }

    return render(request, 'by_products.html', context)# About Page 

@login_required(login_url='home_login')
def About (request):  
    cart_items = Cart.objects.filter(
        user=request.user
    )
    cart_quantity = 0

    for item in cart_items:
     cart_quantity += item.quantity

    total = 0

    for item in cart_items:
        total += item.quantity * item.Product.final_price

    context = {
        'cart_items': cart_items,
        'total': total,
        'cart_quantity': cart_quantity,
    }
  
    return render(request,'about.html',context)

# admin user page 
def admin_user (request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)    
        if user is not None and user.is_superuser:
            login(request,user)
            return redirect('admin_orders')
        else:
            messages.error(request,'your are Not Admin user')      
    return render(request,'admin_login.html')

# Admin logout view 
def logout_view(request):
    # Logs out the user
    logout(request)
    
    # Redirect to homepage (or login page)
    return redirect('home')  # replace 'home' with your url name

# home logout view Admin
def logout_home(request):
    
    logout(request)
    return redirect('home_login')  


# Admin Show product in Admin
@login_required
def admin_show(request):
    data = add_product.objects.all()
    return render(request,'admin_show.html',{'data':data})

# Admin add Products
@login_required
def add_products(request):
    if request.method == 'POST':
        Flower = request.POST.get('Flower')
        rate = int(request.POST.get('rate'))
        discount = int(request.POST.get('discount'))
        qut = request.POST.get('qut')
        imge = request.FILES.get('imge')
        
        add_product.objects.create(
            Flower=Flower,
            rate=rate,
            discount=discount,
            qut=qut,
            imge=imge
        )
        
        messages.success(request, 'you Items is add in admin')
        return redirect('admin_show')
        
    else:
        messages.error(request, 'you item is not add in admin')        
        return render(request, 'add_product.html')

# dele View of show 
def delete_product(request, id):
    product = add_product.objects.get(id=id)
    product.delete()
    return redirect('admin_show')


# Edite view 
from django.shortcuts import render, redirect, get_object_or_404
@login_required
def edit_product(request, id):
    product = get_object_or_404(add_product, id=id)

    if request.method == 'POST':
        product.Flower = request.POST.get('Flower')
        product.rate = int(request.POST.get('rate', 0))
        product.discount =int(request.POST.get('discount', 0))
        product.qut = int(request.POST.get('qut', 0))

        # Update image only if a new one is selected
        if 'imge' in request.FILES:
            product.imge = request.FILES['imge']


        product.save()
        return redirect('admin_show')

    return render(request, 'edit_product.html', {'product': product})

# Flower Detales 
@login_required(login_url='home_login')
def Flower_detales(request,my_id):

    data1 = get_object_or_404(add_product,pk=my_id)
    
    return render(request,'Dettles.html',{'data1':data1})
# home account page
def home_account (request):
    
    if request.method == 'POST':
        # username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if password != password2:
            messages.error(request,'password is not match')
            return render(request,'home_account.html')
        
        if len(password) < 8:
            
          messages.error(request, 'Password must be at least 8 characters long.')
          return render(request,'home_account.html')  # replace with your URL name
        
        
        if User.objects.filter(email=email).exists():
            messages.error(request,'Emale id Exists \n You Chose Defrant Emaile')
            return render(request,'home_account.html')
        
        # User.objects.create_user(username = email, email = email, password = password)
        otp = random.randint(100000, 999999)
        
        request.session['otp'] = str(otp)
        request.session['email'] = email
        request.session['password'] = password
        
        send_mail(
            'Flower shop OTP verification',
            f'Your otp is {otp}',
            'anmolsingh248670@gmail.com',
            [email]
            
        )
        
        return redirect('verify_otp')
       
    
    return render(request,'home_account.html')

# verify_otp
def verrify_otp (request):
    
    if request.method == "POST":
        
        user_otp = request.POST.get('otp')
        
        if user_otp == request.session.get("otp"):
            
            User.objects.create_user(
                username=request.session.get('email'),
                email=request.session.get('email'),
                password=request.session.get('password')
            )
            
            del request.session['otp']
            del request.session['email']
            del request.session['password']
            
            messages.success(request,"Account Create Successfully!")
            
            return redirect('home_login')
        else:
            messages.error(request,'Invalid OTP')
            
    return render(request,'verify_otp.html')        
            

# home_Login page 

def home_login(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(
                request,
                username=user_obj.username,
                password=password
            )

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid Password')

        except User.DoesNotExist:
            messages.error(request, 'Email Not Found')

    return render(request, 'home_login.html')


#  Add to Cart


@login_required(login_url='home_login')
def add_to_cart(request, id):

    product = get_object_or_404(add_product, id=id)

    if product.qut <= 0:
        messages.error(request, "Stock Over")
        return redirect('products')

    cart_item = Cart.objects.filter(
        user=request.user,
        Product=product
    ).first()

    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
    else:
        Cart.objects.create(
            user=request.user,
            Product=product,
            quantity=1
        )

    product.qut -= 1
    product.save()

    messages.success(request, "Added To Cart")

    return redirect('products')


# Cart puls
@login_required(login_url='home_login')
def plus_cart(request, id):

    cart_item = get_object_or_404(Cart, id=id)
    if cart_item.Product.qut <= 0:
        messages.error(request, "Stock Over")
        return redirect('products')

    if cart_item.Product.qut > 0:

        cart_item.quantity += 1
        cart_item.save()

        cart_item.Product.qut -= 1
        cart_item.Product.save()

    return redirect('products')


# cart mines
@login_required(login_url='home_login')
def minus_cart(request, id):

    cart_item = get_object_or_404(Cart, id=id)

    if cart_item.quantity > 1:

        cart_item.quantity -= 1
        cart_item.save()

        cart_item.Product.qut += 1
        cart_item.Product.save()
    else:
        cart_item.Product.qut += 1
        cart_item.Product.save()

        cart_item.delete()    

    return redirect('products')


# Review page 
@login_required(login_url='home_login')
def review(request):
    
    if request.method == "POST":
        rating=request.POST.get("rating")
        comment=request.POST.get("comment")
        
        
        Review.objects.create(
            user=request.user,
            rating= rating,
            comment = comment
        )
        return redirect('review')
    
    reviews = Review.objects.filter(user=request.user)
    
    cart_items = Cart.objects.filter(
        user=request.user
    )
    cart_quantity = 0

    for item in cart_items:
     cart_quantity += item.quantity

    total = 0

    for item in cart_items:
        total += item.quantity * item.Product.final_price

    context = {
        'reviews': reviews,
        'cart_items': cart_items,
        'total': total,
        'cart_quantity': cart_quantity,
    }

    


    return render(request, "review.html",context)

# chek out page

   

def Chek_out(request):
     # Prevent admin users from creating/updating addresses
     if request.user.is_staff or request.user.is_superuser:
         return redirect("home_login")   # Change "home" to your desired page

     if request.method == "POST":
        full_name=request.POST.get("full_name")
        phone=request.POST.get("phone")
        house_no=request.POST.get("house_no")
        street=request.POST.get("street")
        city=request.POST.get("city")
        state=request.POST.get("state")
        pincode=request.POST.get("pincode")
        country=request.POST.get("country")
        
         # Check if the user already has an address
        address = Adders.objects.filter(user=request.user).first()

        if address:
            # Update existing address
            address.full_name = full_name
            address.phone = phone
            address.house_no = house_no
            address.street = street
            address.city = city
            address.state = state
            address.pincode = pincode
            address.country = country
            address.save()
        else:
            # Create new address
            Adders.objects.create(
                user=request.user,
                full_name=full_name,
                phone=phone,
                house_no=house_no,
                street=street,
                city=city,
                state=state,
                pincode=pincode,
                country=country,
            )
      
        
        
        return redirect("payment")   # or "order_success"
      
     data = Cart.objects.filter(user=request.user)
     
     total = 0

     for item in data:
        total += item.quantity * item.Product.final_price
           
     return render(request, "chek_out.html",{'data':data,'total':total})  


# payment page
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from datetime import date, timedelta
def payment (request):
    
    if request.method == 'POST':
      payment_method = request.POST.get('payment_method')
      request.session["payment_method"] = payment_method
      
      if payment_method == "COD":
       
         return redirect('Place_Order')
    
      elif payment_method == 'Online':
         return redirect('razorpay_payment')
    
    address = Adders.objects.filter(user=request.user).first()
    today = date.today()
    delivery_date = today + timedelta(days=7)
    
    data = Cart.objects.filter(user=request.user)
     
    total = 0

    for item in data:
        total += item.quantity * item.Product.final_price
    
    

    return render(request,'Payment.html',{'address':address,"delivery_date": delivery_date,'total':total,'data':data}) 

# Place Order

from datetime import date, timedelta
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

@login_required
def Place_Order(request):

    data = Cart.objects.filter(user=request.user)
    address = Adders.objects.filter(user=request.user).first()

    today = date.today()
    delivery_date = today + timedelta(days=7)

    total = 0
    for item in data:
        total += item.quantity * item.Product.final_price

    # ==========================
    # Create Order
    # ==========================
    payment_method = request.session.get("payment_method", "COD")

    order = Order.objects.create(
        user=request.user,
        address=address,
        total_price=total,
        payment_method=payment_method,
        delivery_date=delivery_date,
        status="Pending"
    )

    # ==========================
    # Save Order Products
    # ==========================

    for item in data:
        OrderItem.objects.create(
            order=order,
            product=item.Product,
            quantity=item.quantity,
            price=item.Product.final_price
        )

    # ==========================
    # Send Email
    # ==========================

    html = render_to_string(
        "text.html",
        {
            "order": order,
            "data": data,
            "address": address,
            "delivery_date": delivery_date,
            "total": total,
        },
    )

    email = EmailMultiAlternatives(
        subject="Order Confirmation",
        body="",
        from_email="anmolsingh248670@gmail.com",
        to=[
            request.user.email,
            "anmolsingh248670@gmail.com",
        ],
    )

    email.attach_alternative(html, "text/html")
    email.send()

    # ==========================
    # Clear Cart
    # ==========================

    Cart.objects.filter(user=request.user).delete()
    
    if "payment_method" in request.session:
        del request.session["payment_method"]

    return render(
        request,
        "Place_order.html",
        {
            "order": order,
            "data": data,
            "address": address,
            "delivery_date": delivery_date,
            "total": total,
        },
    )    # send Email user and me
    
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Order

@login_required(login_url='home_login')
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    data = add_product.objects.all()
    cart_items = Cart.objects.filter(
        user=request.user
    )
    cart_quantity = 0

    for item in cart_items:
     cart_quantity += item.quantity

    total = 0

    for item in cart_items:
        total += item.quantity * item.Product.final_price

    context = {
        'data':data,
        'orders': orders,
        'cart_items': cart_items,
        'total': total,
        'cart_quantity': cart_quantity,
    }

    
    return render(request, 'orders.html',context)


#  Oneline payment
import razorpay
from django.conf import settings
from django.shortcuts import render
from .models import Cart

def razorpay_payment(request):

    cart = Cart.objects.filter(user=request.user)

    total = 0
    for item in cart:
        total += item.quantity * item.Product.final_price

    client = razorpay.Client(
        auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET)
    )

    order = client.order.create({
        "amount": total * 100,
        "currency": "INR",
        "payment_capture": 1
    })

    context = {
        "razorpay_key": settings.RAZORPAY_KEY_ID,
        "order_id": order["id"],
        "amount": order["amount"],
        "total": total,
    }

    return render(request, "razorpay_payment.html", context) 

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .models import Contact

@login_required(login_url='home_login')
def contact(request):

    if request.method == "POST":

        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        Contact.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            subject=subject,
            message=message,
        )

        # Email to website owner
        send_mail(
            subject=f"New Contact: {subject}",
            message=f"""
Name: {full_name}

Email: {email}

Phone: {phone}

Subject: {subject}

Message:
{message}
""",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
        )

        # Thank you email to customer
        send_mail(
            subject="Thank You for Contacting Bloomy Flowers",
            message=f"""
Hello {full_name},

Thank you for contacting Bloomy Flowers.

We have received your message and will reply as soon as possible.

Have a wonderful day!

Bloomy Flowers Team
""",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
        )

        messages.success(request, "Message sent successfully!")

        return redirect("contact")
    cart_items = Cart.objects.filter(
        user=request.user
    )
    cart_quantity = 0

    for item in cart_items:
     cart_quantity += item.quantity

    total = 0

    for item in cart_items:
        total += item.quantity * item.Product.final_price

    context = {
        'cart_items': cart_items,
        'total': total,
        'cart_quantity': cart_quantity,
    }


    return render(request, "contact.html",context) 



from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Order

@staff_member_required
def admin_orders(request):

    search = request.GET.get("search")

    if search:
        orders = Order.objects.filter(
            user__username__icontains=search
        ) | Order.objects.filter(
            id__icontains=search
        )
    else:
        orders = Order.objects.all().order_by("-created_at")

    return render(request, "admin_orders.html", {
        "orders": orders
    })


@staff_member_required
def update_order(request, id):

    order = get_object_or_404(Order, id=id)

    if request.method == "POST":

        order.status = request.POST.get("status")
        order.save()

    return redirect("admin_orders")
 
 
from django.shortcuts import render, redirect
from .models import Detales, add_product

def add_details(request):
    if request.method == "POST":
        print(request.POST)  # Debug

        product = add_product.objects.get(id=request.POST.get("detales"))
        Detales.objects.update_or_create(
    detales=product,
    defaults={
        "header": request.POST.get("header"),
        "Color": request.POST.get("Color"),
        "text": request.POST.get("text"),
        "date": request.POST.get("date"),
    }
)

        # Detales.objects.create(
        #     detales=product,
        #     header=request.POST.get("header"),
        #     Color=request.POST.get("Color"),
        #     text=request.POST.get("text"),
        #     date=request.POST.get("date"),
        # )

        return redirect("admin_orders")

    products = add_product.objects.all()
    return render(request, "add_details.html", {"products": products})

# Profile start
from .models import Profile

def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    total_orders = Order.objects.filter(user=request.user).count()

    total_addresses = Adders.objects.filter(user=request.user).count()

    cart_items = Cart.objects.filter(user=request.user).count()

    total_spent = sum(
    order.total_price for order in Order.objects.filter(user=request.user)
    )
    
    if request.method == "POST":

        profile.phone = request.POST.get("phone")
        profile.dob = request.POST.get("dob")
        profile.gender = request.POST.get("gender")
        profile.name = request.POST.get("name")

        if request.FILES.get("image"):
            profile.image = request.FILES["image"]

        profile.save()


    context = {
    "profile": profile,
    "total_orders": total_orders,
    "total_addresses": total_addresses,
    "cart_items": cart_items,
    "total_spent": total_spent,
}

    return render(request, "profile.html", context)

# like 
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Wishlist, add_product

@login_required
def toggle_wishlist(request, id):
    product = get_object_or_404(add_product, id=id)

    wishlist_item = Wishlist.objects.filter(
        user=request.user,
        product=product
    )

    if wishlist_item.exists():
        wishlist_item.delete()
    else:
        Wishlist.objects.create(
            user=request.user,
            product=product
        )

    return redirect(request.META.get("HTTP_REFERER", "home"))

def wishlist(request):
    items = Wishlist.objects.filter(user=request.user)

    context = {
        "items": items
    }
    return render(request, "wishlist.html", context) 