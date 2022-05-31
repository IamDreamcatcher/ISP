from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from app.tokens import account_activation_token


def send_activate_link(user, request):
    current_site = get_current_site(request)
    subject = 'Activate your account.'
    message = render_to_string('auth/activate_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    })
    return send_mail(subject, message, 'dreamrestik', [user.email], fail_silently=False)
