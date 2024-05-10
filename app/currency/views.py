from currency.forms import ContactUSForm, RateForm, SourceForm
from currency.models import Rate, Source
from currency.utils import generate_password as gp

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
# from django.shortcuts import render


def generate_password(request):
    password = gp()
    return HttpResponse(password)


def rate_list(request):
    queryset = Rate.objects.all()
    # ids = []
    # from time import time

    # for rate in queryset:
    #     ids.append(rate.id)

    context = {
        'objects': queryset,
    }

    return render(request, 'rate_list.html', context=context)


def rate_details(request, pk):

    # try:
    #     rate = Rate.objects.get(pk=pk)
    # except Rate.DoesNotExist:
    #     raise Http404(f"Rate does not exist with id: {pk}")

    rate = get_object_or_404(Rate, pk=pk)

    context = {
        'object': rate,
    }
    return render(request, 'rate_details.html', context=context)


def source_list(request):
    queryset = Source.objects.all()

    context = {
        'sources': queryset,
    }

    return render(request, 'souce_list.html', context=context)


def sourse_details(request, pk):

    source = get_object_or_404(Source, pk=pk)

    context = {
        'source': source,
    }

    return render(request, 'source_details.html', context=context)


def rate_create(request):

    if request.method == 'POST':
        form_data = request.POST
        form = RateForm(form_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/currency/rate/list/')
    elif request.method == 'GET':
        form = RateForm()

    context = {
        'massage': 'Rate Create',
        'form': form,
    }

    return render(request, 'rate_create.html', context=context)


def rate_update(request, pk):

    instance = get_object_or_404(Rate, pk=pk)
    if request.method == 'POST':
        form_data = request.POST
        form = RateForm(form_data, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/currency/rate/list/')
    elif request.method == 'GET':
        form = RateForm(instance=instance)

    context = {
        'massage': 'Rate Update',
        'form': form,
    }

    return render(request, 'rate_update.html', context=context)


def rate_delete(request, pk):
    instance = get_object_or_404(Rate, pk=pk)
    if instance is not Http404:
        instance.delete()
    return HttpResponseRedirect('/currency/rate/list/')


def contact_us_create(request):
    if request.method == 'POST':
        form_data = request.POST
        form = ContactUSForm(form_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/currency/rate/list/')
    else:
        form = ContactUSForm()

    context = {
        'massage': 'Contact Us',
        'form': form,
    }
    return render(request, 'contact_us_create.html', context=context)


def soucre_create(request):
    if request.method == 'POST':
        form_data = request.POST
        form = SourceForm(form_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/currency/source/list/')
    else:
        form = SourceForm()

    context = {
        'massage': 'Source Create',
        'form': form,
    }
    return render(request, 'source_create.html', context=context)


def source_update(request, pk):
    instance = get_object_or_404(Source, pk=pk)
    if request.method == 'POST':
        form_data = request.POST
        form = SourceForm(form_data, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/currency/source/list/')
    else:
        form = SourceForm(instance=instance)

    context = {
        'massage': 'Source Update',
        'form': form,
    }
    return render(request, 'source_update.html', context=context)


def source_delete(request, pk):
    instance = get_object_or_404(Source, pk=pk)
    if instance is not Http404:
        instance.delete()
    return HttpResponseRedirect('/currency/source/list/')
