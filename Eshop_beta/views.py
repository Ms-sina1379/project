from django.shortcuts import render, redirect


def home_page(request):
    context = {
        "data": 'data'
    }
    return render(request, 'shared/esh_home.html', context)


def header(request):
    context = {

    }
    return render(request, 'shared/header.html', context)


def footer(request):
    context = {

    }
    return render(request, 'shared/Footer.html', context)
