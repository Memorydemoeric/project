from django.shortcuts import render

# Create your views here.


def system_manage(request):
    data = {}
    return render(request, 'system_manage.html', data)