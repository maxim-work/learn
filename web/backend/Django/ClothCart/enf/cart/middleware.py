from django.utils.deprecation import MiddlewareMixin
from .models import Cart

class CartMiddleware(MiddlewareMixin):
    def process_requst(self, request):
        if not request.session.session_key:
            request.session.create()

        request.cart, create = Cart.objects.get_or_create(
            session_key=request.session.session_key
        )

        return None