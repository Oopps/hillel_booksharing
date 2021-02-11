
from time import time

from books.models import Log


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time()

        response = self.get_response(request)
        end = time()
        time_dif = end - start
        Log.objects.create(path=str(request.path), method=str(request.method), time=time_dif)
        return response
