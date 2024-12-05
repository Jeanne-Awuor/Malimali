from .cart import Cart


#Create context processor so that cart can work on all pages
#Remember to add 'cart.context_processors.cart' in settings.py under templates
def cart(request):
    # Return the default data from our cart
    return {'cart' : Cart(request)}
