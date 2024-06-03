from django.http import JsonResponse
from django.conf import settings
from sklearn.feature_extraction.text import TfidfVectorizer
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt #disable temporary
def checkFact(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        text = body['text']
        print(text)
        if text in (None, ''):
            return JsonResponse({'prediction': "Please input text"})
        else:
            text = [text]
            model = settings.MODEL
            pred = model.predict(text)
            print(pred)
            if pred[0] == 0:
                return JsonResponse({'prediction': "Valid"})
            elif pred[0] == 1:
                return JsonResponse({'prediction': "Hoax"})
            return JsonResponse({'prediction': pred})