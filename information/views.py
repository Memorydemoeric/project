from django.shortcuts import render

# Create your views here.


def info_manage(request):
    data = {}
    return render(request, 'info_manage.html', data)