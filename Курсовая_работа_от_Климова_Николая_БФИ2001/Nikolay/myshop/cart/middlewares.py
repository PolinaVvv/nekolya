# cart/middlewares.py

from cart.cart import Cart
from django.utils.translation import get_language

class CartMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        last_language = request.session.get('last_language')
        current_language = get_language()

        # Если язык изменился, обновляем корзину
        if last_language != current_language:
            cart = Cart(request)
            cart.update_prices()
            request.session['last_language'] = current_language

        response = self.get_response(request)
        return response
