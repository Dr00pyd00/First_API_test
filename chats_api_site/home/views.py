from django.shortcuts import render

# Create your views here.


def CatList(request):
    return render(request, 'home/api_list.html')