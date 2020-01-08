from django.shortcuts import render
from django.contrib.auth.models import User
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created

def order_create(request):
    cart = Cart(request)
    first_name = request.user.get_short_name
    username = request.user.username
    email = request.user.email
    print('email',email)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity = item['quantity'])
            cart.clear()
            #launch aysnchronous tasks
            order_created.delay(order.id)
            context = {'first_name':first_name,
            'username':username,
            'email':email,
            'order':order,}
            return render(request,'orders/order/created.html',context)
    else:
        form = OrderCreateForm()
        form.fields["email"].initial = email
        form.fields["first_name"].initial = first_name
        form.fields["username"].initial = username
        context = {
        'cart':cart,
        'form':form,
        'first_name':first_name,
        'username':username,
        'email':email,
        }
        return render(request,'orders/order/create.html',context)
