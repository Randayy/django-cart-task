from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cart.cart import Cart
from cart.models import Product

class CartAPIView(APIView):
    
    def get(self, request):
        cart = Cart(request)
        data = []
        for item in cart:
            data.append({
                'product_id': item['product'].id,
                'name': item['product'].name,
                'quantity': item['quantity'],
                'price': item['price'],
                'total_price': item['total_price'],
            })
        return Response(data)

    def post(self, request):
        """
        Очікує JSON: { "product_id": 1, "quantity": 2 }
        """
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))
        
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        cart = Cart(request)
        cart.add(product, quantity)
        return Response({'message': 'Added to cart'})

    def delete(self, request, product_id):
        cart = Cart(request)
        product_id = str(product_id)
        if product_id in cart.cart:
            cart.remove(product_id)
            return Response({'message': 'Removed from cart'})
        else:
            return Response({'error': 'Product not in cart'}, status=404)
