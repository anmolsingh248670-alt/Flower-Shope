from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class add_product(models.Model):
    Flower = models.CharField(max_length=20)
    rate = models.IntegerField()
    discount = models.IntegerField()
    qut = models.IntegerField()
    imge = models.ImageField(upload_to='products/')
    final_price = models.IntegerField(blank=True, null=True)  # store final price
    

    def save(self, *args, **kwargs):
        # calculate final_price automatically
        if self.rate and self.discount:
            self.final_price = int(
            self.rate - (self.rate * self.discount / 100)
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.Flower
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Product = models.ForeignKey(add_product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date = models.DateField(default=timezone.now())
    
    
class Detales(models.Model):
    detales = models.OneToOneField(add_product,on_delete=models.CASCADE,related_name='Flower_ditales')  
    header = models.CharField(max_length=150)  
    Color = models.CharField(max_length=20)
    text = models.TextField()
    date = models.DateField(default=timezone.now())
    
    def __str__(self):
        return f'Flower Detailes {self.detales}'
    
    
    
    
    #  Addres Models
    


class Adders(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
  
    full_name = models.CharField(max_length=50)
    # email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    house_no = models.CharField(max_length=200)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    country = models.CharField(max_length=90)
    date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.full_name    
    
    
    #  Send user Dlvery detales and send 2 email me Where is delver Order
    

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username    
    

class Order(models.Model):
    
    PAYMENT_METHODS = (
        ("COD", "Cash on Delivery"),
        ("Online", "Online Payment"),
    )

    STATUS = (
    ("Pending", "Pending"),
    ("Processing", "Processing"),
    ("Shipped", "Shipped"),
    ("Delivered", "Delivered"),
    ("Cancelled", "Cancelled"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Adders, on_delete=models.SET_NULL, null=True)
    total_price = models.IntegerField()
    payment_method = models.CharField(max_length=20,choices=PAYMENT_METHODS, default="COD")
    delivery_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(add_product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.product.Flower}"    
    
    #  Contect Model

class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name    
    
    
    #  this is models for user profile 
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True)
    dob = models.DateField(blank=True, null=True)

    GENDER = (
        ("Male", "Male"),
        ("Female", "Female"),
    )

    gender = models.CharField(max_length=10, choices=GENDER, blank=True)

    def __str__(self):
        return self.user.username    
    
    # 
    
from django.db import models
from django.contrib.auth.models import User

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(add_product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user.username} - {self.product.Flower}"