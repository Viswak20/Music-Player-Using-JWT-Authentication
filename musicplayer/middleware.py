import re
from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.exempt_urls = [
            re.compile(r'^/$'),
            re.compile(r'^/signup/$'),
            re.compile(r'^/api/login/$'),
            re.compile(r'^/admin/'),
            re.compile(r'^/static/'),
            re.compile(r'^/media/'),
        ]

    def __call__(self, request):
        path = request.path

        if any(pattern.match(path) for pattern in self.exempt_urls):
            return self.get_response(request)

        if 'jwt' not in request.session:
            return redirect(f"{reverse('login')}")

        return self.get_response(request)
