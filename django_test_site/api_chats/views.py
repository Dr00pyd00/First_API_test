from django.shortcuts import render
from django.http import JsonResponse
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


data_chats = [
        {'name':'Biscotte', 'age':3},
        {'name':'Gulli', 'age':7},
        {'name':'Bibi', 'age':13},
        {'name':'Sushi', 'age':5},
        {'name':'Kiki', 'age':65},
        {'name':'Dolly', 'age':5},
    
]

@csrf_exempt
def ChatsListApi(request):
    if request.method == 'GET':
        return JsonResponse(data_chats, safe=False)
    
    elif request.method == 'POST':
        body_text = request.body.decode('utf-8') # je prend ce que je recois en binaire et je le convertie en texte
        body_data = json.loads(body_text)   # je le transform de json => dict python
        print(body_data)    
        data_chats.append(body_data)       # je l'ajoute a la data
        return JsonResponse({'message':'Chat ajouté !'})



