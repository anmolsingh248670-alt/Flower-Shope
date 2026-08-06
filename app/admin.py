from django.contrib import admin
from .models import add_product,Detales,Cart,Adders,Review,Order,Contact,Profile,Wishlist

admin.site.register(Cart)
admin.site.register(Detales)
admin.site.register(add_product)  
admin.site.register(Adders)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(Profile)
admin.site.register(Wishlist)


class Admin_product(admin.ModelAdmin):
    list_display = ('Flower', 'rate', 'discount', 'final_price', 'qut')

admin.site.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = (
        "full_name",
        "email",
        "phone",
        "subject",
        "created_at",
    )

    search_fields = (
        "full_name",
        "email",
        "phone",
    )

    list_filter = (
        "created_at",
    )

    ordering = (
        "-created_at",
    )

# Now every contact message will app    
    
    

   
    
   


  
