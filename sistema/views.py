from django.http import HttpResponse


def keep(request):
    return HttpResponse('Keep Knowing using HttpResponse')

def home(request):
    return HttpResponse('HOME - MAIN PAGE')

def year_filter(request, year):
    r = 'O ano selecionado é {}'.format(year)
    return HttpResponse(r)
