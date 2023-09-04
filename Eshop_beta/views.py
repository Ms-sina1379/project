from django.shortcuts import render, redirect


def Home_page(request):
    context = {
        "data": 'data'
    }
    return render(request, 'esh_home.html', context)
