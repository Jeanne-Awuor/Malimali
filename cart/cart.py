class Cart():
    def __init__(self,request):
        #to manage the customer sessions
        self.session = request.session

        #Get the current session key if it exists
        cart = self.session.get('session_key')

        #if the user is new,no session key,create new one
        if session_key not in request.session:
            cart = self.session['session_key'] = {}


        #Making sure cart is available on all pages of the site
        self.cart = cart
