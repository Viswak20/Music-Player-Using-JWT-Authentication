import jwt
from django.conf import settings
from django.shortcuts import redirect

class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        public_paths = ['/login/', '/signup/', '/static/','/admin/','/api/']
        if any(request.path.startswith(path) for path in public_paths):
            return self.get_response(request)

        token = request.COOKIES.get('jwt')

        if not token:
            return redirect('login')

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            request.user_id = payload.get('user_id')
            request.user_email = payload.get('email')
        except jwt.ExpiredSignatureError:
            return redirect('login')
        except jwt.InvalidTokenError:
            return redirect('login')
