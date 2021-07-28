from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name="ShopHome"),
    path('about/',views.aboutus,name="aboutus"),
    path('contactus/',views.contactus,name="contactus"),
    path('tracker/',views.tracker,name="tracker"),
    path('search/',views.search,name="search"),
    path("products/<int:myid>", views.productview, name="ProductView"),
    path('checkout/',views.checkout,name="checkout"),
]