from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.http import urlsafe_base64_decode
from django.urls import reverse
from django.contrib import messages  # If you want to use messaging framework

User = get_user_model()

def activate_account(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode('utf-8') 
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist) as e:
        return HttpResponse('Activation link is invalid!', status=400)

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        print(user)
        messages.success(request, 'Your account has been activated!')

        return redirect(reverse('activation_success'))
    else:
        return HttpResponse('Activation link is invalid!', status=400)