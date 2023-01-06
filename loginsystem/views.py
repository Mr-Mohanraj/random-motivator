from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import exceptions
from loginsystem.authentication import create_refresh_token
from loginsystem.authentication import decode_refresh_token
from loginsystem.authentication import JWTAuthentication
from loginsystem.authentication import create_access_token
from .models import User, Reset
from .serializers import UserSerializer
from django.core.mail import send_mail
import random
import string
from django.shortcuts import render
from loginsystem.forms import LoginForm, RegisterForm
from rest_framework import status


class RegisterApiView(APIView):
    def get(self, request):
        print("data", request.GET)
        context = {}
        context['from'] = RegisterForm()
        return render(request, 'loginsystem/register.html', context)
    
    def post(self, request):
        data = request.data

        if data['password'] != data['password_confirm']:
            raise exceptions.APIException('Password do not match!')

        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class LoginApiView(APIView):
    def get(self, request):
        print("data", request.GET)
        context = {}
        context['from'] = LoginForm()
        return render(request, 'loginsystem/login.html', context)
    
    
    def post(self, request):
        print("data",request.data)
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            print("insude the")
            raise exceptions.AuthenticationFailed(detail=f"Invalid credentials {status.HTTP_401_UNAUTHORIZED}")

        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('Invalid credentials, check your password')

        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)

        response = Response()

        response.set_cookie(key='refresh_token',
                            value=refresh_token, httponly=True)
        response.data = {
            'token': access_token
        }

        return response


class UserApiView(APIView):
    print("inside the user")
    authentication_classes = [JWTAuthentication]
    def get(self, request):
        print(request.user)
        return Response(UserSerializer(request.user).data)


class RefreshAPIVew(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        id = decode_refresh_token(refresh_token)

        access_token = create_access_token(id)

        return Response({
            'token': access_token
        })


class ForgetAPIView(APIView):
    def post(self, request):
        email = request.data['email']
        token = ''.join(random.choice(string.ascii_lowercase +
                        string.digits) for _ in range(10))

        Reset.objects.create(
            email=email,
            token=token
        )

        url = 'http://127.0.0.1:8899/api/reset/' + token

        send_mail(
            subject='Reset your password',
            message='Click <a href="%s">here</a> to ree your password' % url,
            from_email='from_mail@gmail.com',
            recipient_list=[email]
        )

        return Response({
            'message': 'success'
        })


class ResetAPIView(APIView):
    def post(self, request):
        data = request.data
        print(">>>>>>", data)
        if data['password'] != data['password_confirm']:
            raise exceptions.APIException('Passwords do not match')

        user = User.objects.filter(token=data['token']).first()

        if not user:
            raise exceptions.APIException('Invalid link!')

        user.set_password(data['password'])
        user.save()

        return Response({
            'message': 'success'
        })
