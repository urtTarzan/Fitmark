from django.shortcuts import redirect

class LoginRequiredMiddleware:
    """
    Protege todas as páginas exceto login, cadastro e erro.
    """
    PUBLIC_PATHS = [
        '/', '/login/', '/cadastro/', '/erro-login/', '/admin/', 
        '/introduction/', '/parceria/', '/sobre/'
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path not in self.PUBLIC_PATHS:
            return redirect('/erro-login/')  # sempre com barra final
        return self.get_response(request)