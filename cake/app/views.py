
from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication

from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny,IsAuthenticatedOrReadOnly

from .models import Cake, Shape ,Weight, Category

from .serializers import CakeSerializer, ShapeSerializer ,WeightSerializer, CategorySerializer

from authentication.permissions import IsAdminUser, IsUser

from rest_framework_simplejwt.authentication import JWTAuthentication

class CakeListCreateView(APIView):

    serializer_class = CakeSerializer

    #authentication_classes = [TokenAuthentication]
    
   # permission_classes = [IsAuthenticatedOrReadOnly]

    authentication_classes = [JWTAuthentication, TokenAuthentication]

    def get_permissions(self):

        permissions = []

        if self.request.method == "POST":

            permissions = [IsAdminUser]

        return [permission() for permission in permissions]

    

    def get(self,request,*args,**kwargs):

        cake = Cake.objects.all()

        serializer = self.serializer_class(cake,many = True)

        return Response (serializer.data,status= 200)


    def post(self,request,*args,**kwargs):

        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():

            serializer.save()

            data = {'msg':'cake created sucessfully'}

            return Response(data,status=201)

        return Response(serializer.errors,status=400)


class CakeRetrieveUpdateDestroyView(APIView):

    serializer_class = CakeSerializer

    #authentication_classes = [TokenAuthentication]

    authentication_classes = [JWTAuthentication]

    def get_permissions(self):

        permissions = []

        if self.request.method  in [ 'POST', 'PATCH', 'DELETE']:

            permissions = [IsAdminUser]  

        return [permission() for permission in permissions]


    def get(self,request,*args,**kwargs):

        permissions = []

        id = kwargs.get('id')

        cake = Cake.objects.get(id=id)

        serializer = self.serializer_class(cake)

        return Response(serializer.data,status=200)


    def patch(self,request,*args,**kwargs):

        id = kwargs.get('id')

        cake = Cake.objects.get(id=id)

        serializer = self.serializer_class(cake,data=request.data,partial=True)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data,status=200)

        return Response(serializer.errors,status=400)


    def delete(self,request,*args,**kwargs):

        id = kwargs.get('id')

        cake = Cake.objects.get(id=id)

        cake.delete()

        return Response({'msg':'cake deleted successfully'},status=200)

class ShapeListCreateView(APIView):

    serializer_class = ShapeSerializer

    authentication_classes = [BasicAuthentication]

    def get_permissions(self):

        permissions = []

        if self.request.method == "POST":

            permissions = [IsAdminUser]

        return [permission() for permission in permissions]

    

    def get(self,request,*args,**kwargs):

        shape = Shape.objects.all()

        serializer = self.serializer_class(shape,many = True)

        return Response (serializer.data,status= 200)


    def post(self,request,*args,**kwargs):

        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():

            serializer.save()

            data = {'msg':'shape created sucessfully'}

            return Response(data,status=201)

        return Response(serializer.errors,status=400)

class ShapeRetrieveUpdateDestroyView(APIView):

    serializer_class = ShapeSerializer

    authentication_classes = [BasicAuthentication]


    def get_permissions(self):

        permissions = []

        if self.request.method  in [ 'PATCH', 'DELETE']:

            permissions = [IsAdminUser]  

        return [permission() for permission in permissions]


    def get(self,request,*args,**kwargs):

        permissions = []

        id = kwargs.get('id')

        shape = Shape.objects.get(id=id)

        serializer = self.serializer_class(shape)

        return Response(serializer.data,status=200)


    def patch(self,request,*args,**kwargs):

        id = kwargs.get('id')

        shape = Shape.objects.get(id=id)

        serializer = self.serializer_class(shape,data=request.data,partial=True)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data,status=200)

        return Response(serializer.errors,status=400)


    def delete(self,request,*args,**kwargs):

        id = kwargs.get('id')

        shape = Shape.objects.get(id=id)

        shape.delete()

        return Response({'msg':'shape deleted successfully'},status=200)


class WeightListCreateView(APIView):

    serializer_class = WeightSerializer

    authentication_classes = [BasicAuthentication]

    def get_permissions(self):

        permissions = []

        if self.request.method == "POST":

            permissions = [IsAdminUser]

        return [permission() for permission in permissions]

    

    def get(self,request,*args,**kwargs):

        weight = Weight.objects.all()

        serializer = self.serializer_class(weight,many = True)

        return Response (serializer.data,status= 200)


    def post(self,request,*args,**kwargs):

        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():

            serializer.save()

            data = {'msg':'weight created sucessfully'}

            return Response(data,status=201)

        return Response(serializer.errors,status=400)


    class WeightRetrieveUpdateDestroyView(APIView):

        serializer_class = WeightSerializer

        authentication_classes = [BasicAuthentication]


        def get_permissions(self):

            permissions = []

            if self.request.method  in [ 'PATCH', 'DELETE']:

                permissions = [IsAdminUser]  

            return [permission() for permission in permissions]


        def get(self,request,*args,**kwargs):

            permissions = []

            id = kwargs.get('id')

            weight = Weight.objects.get(id=id)

            serializer = self.serializer_class(weight)

            return Response(serializer.data,status=200)


        def patch(self,request,*args,**kwargs):

            id = kwargs.get('id')

            weight = Weight.objects.get(id=id)

            serializer = self.serializer_class(weight,data=request.data,partial=True)

            if serializer.is_valid():

                serializer.save()

                return Response(serializer.data,status=200)

            return Response(serializer.errors,status=400)


        def delete(self,request,*args,**kwargs):

            id = kwargs.get('id')

            weight = Weight.objects.get(id=id)

            weight.delete()

            return Response({'msg':'weight deleted successfully'},status=200)


class CategoryListCreateView(APIView):

    serializer_class = CategorySerializer

    authentication_classes = [BasicAuthentication]

    def get_permissions(self):

        permissions = []

        if self.request.method == "POST":

            permissions = [IsAdminUser]

        return [permission() for permission in permissions]

    

    def get(self,request,*args,**kwargs):

        category = Category.objects.all()

        serializer = self.serializer_class(category,many = True)

        return Response (serializer.data,status= 200)


    def post(self,request,*args,**kwargs):

        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():

            serializer.save()

            data = {'msg':'category created sucessfully'}

            return Response(data,status=201)

        return Response(serializer.errors,status=400)

    class CategoryRetrieveUpdateDestroyView(APIView):

        serializer_class = CategorySerializer

        authentication_classes = [BasicAuthentication]


        def get_permissions(self):

            permissions = []

            if self.request.method  in [ 'PATCH', 'DELETE']:

                permissions = [IsAdminUser]  

            return [permission() for permission in permissions]


        def get(self,request,*args,**kwargs):

            permissions = []

            id = kwargs.get('id')

            category = Category.objects.get(id=id)

            serializer = self.serializer_class(category)

            return Response(serializer.data,status=200)


        def patch(self,request,*args,**kwargs):

            id = kwargs.get('id')

            category = Category.objects.get(id=id)

            serializer = self.serializer_class(category,data=request.data,partial=True)

            if serializer.is_valid():

                serializer.save()

                return Response(serializer.data,status=200)

            return Response(serializer.errors,status=400)


        def delete(self,request,*args,**kwargs):

            id = kwargs.get('id')

            category = Category.objects.get(id=id)

            category.delete()

            return Response({'msg':'category deleted successfully'},status=200)


        