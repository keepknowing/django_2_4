from django.http import HttpResponse


def keep(request):
    return HttpResponse('Keep Knowing using HttpResponse')