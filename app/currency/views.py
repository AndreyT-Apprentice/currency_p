from django.http import HttpResponse
# from django.shortcuts import render

from currency.utils import generate_password as gp


def generate_password(request, ):
    password = gp()
    return HttpResponse(password)
