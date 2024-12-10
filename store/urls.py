from django.urls import path
from . import views



urlpatterns = [
   path('',views.home,name='home'),
   path('about/',views.about,name='about'),
   path('login/',views.login_user,name='login'),
   path('logout/',views.logout_user,name='logout'),
   path('register/',views.register_user,name='register'),
   path('product/<int:pk>',views.product,name='product'),
   path('category/<str:categ>',views.category,name='Category'),
   path('order/<int:product_id>/', views.order_confirmation, name='order_confirmation'),
   path('order/complete/<int:product_id>/', views.complete_order, name='complete_order'),
   path('order/success/<int:product_id>/', views.order_success, name='order_success'),


]