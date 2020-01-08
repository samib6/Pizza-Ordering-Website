from django.shortcuts import render,get_object_or_404
from .models import Category,Product
from cart.forms import CartAddProductForm

def product_list(request,category_slug=None):
    print("entered")
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        # syntax - get_object_or_404 takes first argument as the model name and optional parameters.
        category = get_object_or_404(Category,slug=category_slug)# its a shortcut.
        products = products.filter(category=category)
    cart_product_form = CartAddProductForm()
    context = {
    'category':category,'categories':categories,'products':products,'cart_product_form':cart_product_form
    }
    print('-----------category--------',category)
    print('--------------categories----------',categories)
    print('-----products-----',products)
    return render(request,'Menu/list.html',context)

def product_detail(request,id,slug):
    product = get_object_or_404(Product,id=id,slug=slug,available=True)
    context = {'product':product}
    return render(request,'Menu/detail.html',context)
