from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_prefixes = ['/accounts/', '/admin/', '/password_reset/']
        if not request.user.is_authenticated and not any(request.path.startswith(prefix) for prefix in allowed_prefixes):
            next_url = request.get_full_path()
            return redirect(reverse('account_login') + '?next=' + next_url)
        response = self.get_response(request)
        return response

