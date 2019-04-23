from django.shortcuts import render

# Create your views here.


def sales_manage(request):
    data = {}
    return render(request, 'sales_manage.html', data)