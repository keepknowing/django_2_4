from django.http import HttpResponse
from django.shortcuts import render # new line to use render in template/index.html


def keep(request):
    return HttpResponse('Keep Knowing using HttpResponse')

def home(request):
    return HttpResponse('HOME - MAIN PAGE')

def year_filter(request, year):
    r = 'O ano selecionado é {}'.format(year)
    return HttpResponse(r)

def dados(request):
    return render(request,'index.html')