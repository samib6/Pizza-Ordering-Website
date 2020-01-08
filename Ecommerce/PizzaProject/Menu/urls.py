from django.urls import path
from . import views

app_name = 'Menu'

urlpatterns = [
# to capture a value from the url use the angle brackets.
    path('',views.product_list,name='product_list'),
    path('<slug:category_slug>/',views.product_list,name='product_list_by_category'),
    path('<int:id>/<slug:slug>',views.product_detail,name='product_detail'),
]
#path converters:
#str
#int
#slug
#path
#uuid

# app_name is liek your real name wereas namespaces are the nickname
# or instances . refer docs for example.

# namespaces for url confs and app_name for reverse
