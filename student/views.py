from rest_framework.generics import GenericAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# #list and create -Not Required pk
# class LCBookAPI(GenericAPIView,ListModelMixin,CreateModelMixin):
#     queryset=Book.objects.all()
#     serializer_class=BookSerializer
#
#     def get(self,request,*args,**kwrgs):
#         return self.list(request,*args,**kwrgs)
#
#     def post(self,request,*args,**kwrgs):
#         return self.create(request,*args,**kwrgs)
#
# #retrieve,update and delete,
# class RUSBookAPI(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
#     queryset=Book.objects.all()
#     serializer_class=BookSerializer
#
#     def get(self,request,*args,**kwrgs):
#         return self.retrieve(request,*args,**kwrgs)
#
#     def put(self,request,*args,**kwrgs):
#         return self.update(request,*args,**kwrgs)
#
#     def delete(self,request,*args,**kwrgs):
#         return self.destroy(request,*args,**kwrgs)

class BookAPI(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            bk=Book.objects.get(id=id)
            serializer=BookSerializer(bk)
            return Response(serializer.data)
        bk = Book.objects.all()
        serializer = BookSerializer(bk,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   



    def put(self,request,pk=None,format=None):
        id=pk
        bk=Book.objects.get(pk=id)
        serializer=BookSerializer(bk,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



    def patch(self,request,pk,format=None):
        id=pk
        bk=Book.objects.get(pk=id)
        serializer=BookSerializer(bk,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': ' Partial Data Updated'})
        return Response(serializer.errors)

    def delete(self,request,pk,format=None):
        id=pk
        bk=Book.objects.get(pk=id)
        bk.delete()
        return Response({'msg':'Data Deleted'})