
from django.shortcuts import render
from django.http import HttpResponse

def saludar_con_html(request):

    http_response = render(
        request=request,
        template_name='inicio.html',
    )
    return http_response

def Acerca_de_mi(request):

    http_response = render(
        request=request,
        template_name='Acerca_de_mi.html',
    )
    return http_response