<<<<<<< HEAD:Music-Player-Using-JWT-Authentication/musicplayer/middleware.py
from django.conf import settings
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

class SelectiveAppendSlashMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Define which paths should auto-append slash
        urls_with_slash = ["/route1"]

        if request.path in urls_with_slash and not request.path.endswith("/"):
            return redirect(f"{request.path}/")
        
        return None
=======
import jwt
from django.conf import settings
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
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
        except (ExpiredSignatureError, InvalidTokenError):
            return redirect('login')

        return self.get_response(request)
>>>>>>> ba151df64496fd9290701bf55554bc8884a122c8:musicplayer/middleware.py
