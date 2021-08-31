from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.status import HTTP_201_CREATED
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from .models import Contact
# Create your views here.


class ContactView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        email = request.data.get("email")
        phone = request.data.get("phone")
        message = request.data.get("message")
        context ={
          "first_name":first_name,
"last_name":last_name,
"email":email,
"phone":phone,
"message":message,

        }
        template = render_to_string('email.html', context)
        email = EmailMessage(
             'We have a new Contact mail',
             template,
               settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL]
        )
        email.fail_silently = False
        email.send()
        return Response(status=HTTP_201_CREATED)
        
        

