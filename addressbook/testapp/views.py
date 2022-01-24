from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class CreateAddress(APIView):
    def post(self, request):
        try:
            lat=request.data.get("latitude")
            long=request.data.get("longitude")
            if lat and long:
                address_save = Address(latitude=lat,longitude=long)
                address_save.save()
                return Response({"status": True,"detail": "Your Address Saved Successfully","ID":address_save.id})
            else:
                return Response({"status": False,"detail": "Please Enter Valid Address"})
        except Exception as e:
            return Response({
                'status': False,
                'detail': "something went wrong"
            })

class AddressDetails(APIView):
    def get(self, request):
        try:
            if Address.objects.filter(id=request.data['id']):
                address=Address.objects.get(id=request.data['id'])
                response = {
                'message': 'Address fetched successfully',
                'data': [{
                    'latitude': address.latitude,
                    'longitude': address.longitude,
                    }]}
                return Response({"status": True,"Customer": response })
            else:
                return Response({
                'status': False,
                'detail': "Please Enter Valid ID"
            })
        except:
            return Response({
                'status': False,
                'detail': "something went wrong"
            })

class AddressEdit(APIView):
   def put(self,request):
        try:
            if Address.objects.filter(id=request.data['id']):
                ad_edit = Address.objects.get(id=request.data.get("id"))
                ad_edit.latitude = request.data.get("latitude")
                ad_edit.longitude = request.data.get("longitude")
                ad_edit.save()
                return Response(
                {
                'status' : True,
                'detail' : 'Address Updated Successfully',
                })
            else:
                return Response({
                'status': False,
                'detail': "Please Enter Valid ID"
            })
        except:
            return Response({
                'status': False,
                'detail': "something went wrong"
            })

class DeleteAddress(APIView):
    def post(self,request):
        try:
            id=request.data.get("id")
            if Address.objects.filter(id=id):
                ad_edit = Address.objects.get(id = id)
                #ad_edit.is_deleted = "y"
                ad_edit.delete()
                return Response(
                {
                'status' : True,
                'detail' : 'Address Deleted Successfully',
                })
            else:
                return Response({
                'status': False,
                'detail': "Please Enter Valid ID"
            })
        except:
            return Response({
                'status': False,
                'detail': "something went wrong"
            })