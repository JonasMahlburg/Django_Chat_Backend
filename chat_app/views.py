from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from chat_app.models import Chat
import json


def chat_view(request):
        if request.method == 'GET':
            chats = list(Chat.objects.values())
            return JsonResponse(chats, safe=False)
        

        elif request.method == 'POST':
            data = json.loads(request.body)

            # Optional: einfache Validierung
            if 'name' in data and 'message' in data:
                Chat.objects.create(name=data['name'], message=data['message'])
                return JsonResponse({"status": "success", "added": data})
            else:
                raise Http404()