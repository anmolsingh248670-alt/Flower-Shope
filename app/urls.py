from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('home_account/',views.home_account,name='home_account'),
    path('home_login/',views.home_login,name='home_login'),
    path('verify_otp/',views.verrify_otp,name='verify_otp'),
    path('by_products/',views.by_products,name='products'),
    path('admin_user/', views.admin_user, name='admin_login'),
    path('admin_show/', views.admin_show, name='admin_show'),
    path('admin_show/add_products/', views.add_products, name='add_products'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),
    path('edit/<int:id>/', views.edit_product, name='edit_product'),
    path('admin_logout/',views.logout_view,name='logout'),
    path('About/',views.About,name='About'),
    path('by_products/<int:my_id>/', views.Flower_detales, name='Flower_detales'),
    path('logout_home/',views.logout_home,name='logout_home'),
    path('add_to_cart/<int:id>/',views.add_to_cart,name='cart'),
    path('plus_cart/<int:id>/', views.plus_cart, name='plus_cart'),
    path('minus_cart/<int:id>/', views.minus_cart, name='minus_cart'),
    path('review/',views.review,name='review'),
    path('payment/',views.payment,name='payment'),
    path('Chek_out/',views.Chek_out, name='Chek_out'),
    path('Place_Order/',views.Place_Order, name='Place_Order'),
    path('my-orders/', views.my_orders, name='my_orders'),  
    path("razorpay-payment/",views.razorpay_payment,name="razorpay_payment",),
    path("contact/", views.contact, name="contact"),
    path("admin_orders/", views.admin_orders, name="admin_orders"),
    path("update-order/<int:id>/", views.update_order, name="update_order"),
    path('add_detales/',views.add_details,name='add_detales'),
    path('Profile/',views.profile,name='profile'),
    path('wishlist/<int:id>/', views.toggle_wishlist, name='toggle_wishlist'),
    path('whshilst/',views.wishlist, name="wishlist")
    

    # path('<int:my_id>/',views.Flower_detales,name='Flower_detales'),
  
]

