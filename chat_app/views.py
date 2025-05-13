from django.shortcuts import render
from django.http import HttpResponse, Http404
from chat_app.models import Chat
import json

def chat_view(request):
        if request.method == 'GET':
            return HttpResponse(json.dumps(Chat), content_type="application/json")
        

        elif request.method == 'POST':
            data = json.loads(request.body)

            # Optional: einfache Validierung
            if 'name' in data and 'gewicht' in data and 'farbe' in data:
                fruits.append(data)
                return HttpResponse(json.dumps({"status": "success", "added": data}), content_type="application/json")
            else:
                raise Http404()
        