from django.contrib.auth import get_user_model
from django.shortcuts import render,HttpResponse
User= get_user_model()
from django.contrib.auth import get_user_model
user = get_user_model()
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

class SignupView(APIView):
    print('mmmmmmmmmmmmmmmm')
    permission_classes = (permissions.AllowAny,)

    def post(self,request,format=None):
        print('nnnnnnnnnnnnnnnnnnnnnnnnnnnn')
        data = self.request.data

        name = data['name']
        email =data['email']
        password = data['password']
        password2 = data['password2']
        print('nnnnnnnnnnnnnnnnnnnnnnnnnnnn')
        if password == password2:
            if User.object.filter(email=email).exists():
                return Response({'error':'email exists'})
            else:
                if len(password)<6:
                    return Response({'error':'password must be six charecters'})
                else:
                    user=User.object.create_user(email = email,password=password,name=name)
                    user.save()
                    return Response({'success':'user create successfuly'})
        else:

            return Response({'error':'password do no match'})

