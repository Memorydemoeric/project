from django.shortcuts import render

# Create your views here.


def storage_manage(request):
    data = {}
    return render(request, 'storage_manage.html', data)