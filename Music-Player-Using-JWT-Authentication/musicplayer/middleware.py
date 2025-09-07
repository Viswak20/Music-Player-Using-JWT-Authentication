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