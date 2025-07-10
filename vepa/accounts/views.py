from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from .emails import *
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model



class RegisterAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                send_otp_via_email(serializer.data['email'])
                return Response({
                    'status' : 200,
                    'message' : 'registration succesfully check your email',
                    'data' : serializer.data,
                })
            
            return Response({
                'status' : 400,
                'message' : 'something went wrong',
                'data' : serializer.errors
            })
        
        except Exception as e:
            print(e)
            return Response({
                'status': 500,
                'message': 'Internal Server Error',
                'error': str(e),
            }, status=500) 
        
class VerifyOTP(APIView):
    def post(self , request):
        try:
            data = request.data
            serializer = VerifyAccountSerializer(data = data)
            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']
                user = User.objects.filter(email = email)
                if not user.exists():
                    return Response({
                        'status' : 400,
                        'message' : 'something went wrong',
                        'data' : 'invalid email'
                    })
                if user[0].otp != otp:
                    return Response({
                        'status' : 400,
                        'message' : 'something went wrong',
                        'data' : 'invalid email'
                    })
                
                user = user.first()

                user.is_verified = True
                user.save()
                return Response({
                    'status' : 200,
                    'message' : 'OTP verified',
                    'data' : {},
                })
            
            return Response({
                'status' : 400,
                'message' : 'something went wrong',
                'data' : serializer.errors
            })
        except Exception as e:
            print(e)


User = get_user_model()

class Login(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = User.objects.filter(email=email).first()
        if user is None:
            return Response({'status': 400, 'message': 'User not found'})

        if not user.is_verified:
            return Response({'status': 400, 'message': 'Account not verified'})

        if not user.check_password(password):
            return Response({'status': 400, 'message': 'Invalid password'})

        return Response({'status': 200, 'message': 'Login successful'})
