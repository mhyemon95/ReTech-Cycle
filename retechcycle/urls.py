from django.contrib import admin
from django.urls import path
from ecom import views
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view,name=''), # home page view
    path('logout', LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('customersignup', views.customer_signup_view),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('customerlogin', LoginView.as_view(template_name='customerlogin.html'),name='customerlogin'),
    path('adminclick', views.adminclick_view),
    path('adminlogin', LoginView.as_view(template_name='adminlogin.html'),name='adminlogin'),
    path('customer-home', views.customer_home_view,name='customer-home'),
    

]
