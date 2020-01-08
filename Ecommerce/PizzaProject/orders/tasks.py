from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_created(order_id):
    #task to send an email notification when an order is
    # successfully ccreated.

    order = Order.objects.get(id=order.id)
    subject = 'Order No.{}'.format(order.id)
    message = "Dear {},\n\n You have successfully placed an order.\nYour order id is {}".format(order.first_name,order.id)
    mail_sent = send_mail(subject,message,'admin@PizzaProject.com',[order.email])
    return mail_sent
