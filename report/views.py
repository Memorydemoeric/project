from django.shortcuts import render

# Create your views here.


def report_manage(request):
    data = {}
    return render(request, 'report_manage.html', data)