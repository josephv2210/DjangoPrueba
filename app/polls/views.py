from django.http import HttpResponse


def index(request):
    return HttpResponse("Puto el que lo lea desde djnago")