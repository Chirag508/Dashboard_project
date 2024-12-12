from django.urls import path
from . import views
from django.contrib.auth.views import *

urlpatterns = [
    path('',views.show_dashbord,name='dashboard'),
    path('intro/',views.show_intro,name='intro'),
    path('home/',views.show_home,name='home'),
    path('product/',views.show_product_form,name='product'),
    path('product/delete_product/<int:id>',views.delete_product_data,name='delete_product'),
    path('product/update_product/<int:id>',views.update_product_data,name='update_product'),
    path('register/',views.show_registration_form,name='register'),
    # path('register/login/',views.shoe_login_page,name='login'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
]