#a context processor is a function that receives a request
#object as a parameter and returns a dictionary of objects
#that will be available to all the templates rendered using RequestContext.

from .cart import Cart
def cart(request):
     return {'cart':Cart(request)}
