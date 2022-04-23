from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from store_app.models import Product
from .serializers import ProductSerializer
from dj_rest_auth.views import PasswordResetConfirmView

class LaptopListAPIView(APIView):
    """
        Serializing list of laptops
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        laptops = Product.objects.filter(category__slug__exact='laptop')
        serializer = ProductSerializer(laptops, many=True, context={'request': request})
        return Response(serializer.data)


class MobileListAPIView(APIView):
    """
        Serializing list of mobiles
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        mobile = Product.objects.filter(category__slug__exact='mobile')
        serializer = ProductSerializer(mobile, many=True, context={'request': request})
        return Response(serializer.data)


class ProductRetrieveUpdateDeleteAPIView(APIView):
    """
        Serializing product, update, and delete it
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product, many=False, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        instance = Product.objects.get(id=pk)
        new_product = ProductSerializer(instance=instance, data=request.data)
        if new_product.is_valid():
            new_product.save()
            return Response(new_product.data)
        return Response('Not valid')

    def delete(self, request, pk):
        instance = Product.objects.get(id=pk)
        instance.delete()
        return Response('Deleted successfully')


class ProductSaveAPIView(APIView):
    """
        save a new product using rest api
    """
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        product = ProductSerializer(data=request.data)
        if product.is_valid():
            product.save()
            return Response(product.data)
        return Response('Not valid')


class PassResetConfirmView(PasswordResetConfirmView):
    """
        For preventing conflict between account reset password confirm and api reset confirm view, we have to override
         this view
    """
    success_url = 'password_reset_complete'








