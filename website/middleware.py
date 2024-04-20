from django.http import HttpResponseRedirect

class ComingSoonMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path != '/':
            return HttpResponseRedirect('/')
        response = self.get_response(request)
        return response
 
   