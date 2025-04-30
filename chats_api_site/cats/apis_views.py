from .models import Cat
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt


def ApiCatList(request):
    if request.method == 'GET':
        cats_data = Cat.objects.all().values()
        return JsonResponse(list(cats_data), safe=False)
    
    elif request.method == 'POST':
        data_brut = request.body
        data_decode_json = data_brut.decode('utf-8')
        data_python_dict = json.loads(data_decode_json)
        Cat.objects.create(name=data_python_dict['name'], age=data_python_dict['age'])
        return JsonResponse({'message':'Cat added successfully!'})
    
    
    
# test d'une fonction pour la suppresion:
def ApiCatDelete(request, pk):
    if request.method == 'DELETE':
        cat = Cat.objects.get(pk=pk)
        cat.delete()
        return JsonResponse({'message':'cat deleted!'})
        
        