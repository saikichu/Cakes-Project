from django.conf.locale import da
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from decouple import config
from .serializers import ProfileSerializer
from cake.utils import send_mail
import threading

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):

        username = request.data.get('username')

        password = request.data.get('password')

        try:

            if not username:

                raise ValidationError("Username is required")

            if not password:
                raise ValidationError("Password is required")
            
        except ValidationError as error:

            return Response({"error": str(error)}, status=400)

        user = authenticate(username=username, password=password)

        if user:

            refresh_token = RefreshToken.for_user(user)

            access_token = refresh_token.access_token

            data = {
                "access_token": str(access_token),
                "refresh_token": str(refresh_token),
            }

            return Response(data, status=200)

        return Response({"error": "Invalid username or password"}, status=401)


class RegisterView(APIView):

    serializer_class = ProfileSerializer

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            profile = serializer.save()

            profile.email = profile.username

            profile.save(update_fields=['email'])


            recipient = profile.email

            subject = "Welcome to Cake Project"

            template = "emails/registration.html"

            context = {"name": profile.first_name, "email": recipient, "login_url": config('LOGIN_URL')}

            #send_mail(recipient, template, context, subject)

            thread = threading.Thread(target=send_mail, args=(recipient, template, context, subject))

            thread.start()

            data = {"msg": "User registered successfully"}

            return Response(data,status=201, )

        return Response(serializer.errors, status=400)
