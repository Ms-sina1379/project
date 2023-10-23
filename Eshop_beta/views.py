from django.shortcuts import render, redirect


def home_page(request):
    context = {
        "data": 'data'
    }
    return render(request, 'esh_home.html', context)

def header(request):
    context = {

    }
    return render(request,'shard/header.html',context)


def footer(request):
    context = {

    }
    return render(request, 'shard/Footer.html', context)
