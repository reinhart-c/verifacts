from django.http import JsonResponse
from django.conf import settings
from sklearn.feature_extraction.text import TfidfVectorizer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt #disable temporary
def checkFact(request):
    if request.method == 'POST':
        # text = request.POST.get('text')
        text = request.POST.get('text', 'babi terbang menuju angkasa')
        # text = request.POST['text']
        text = [text]
        print(text)
        vectorizer = TfidfVectorizer()
        text = vectorizer.fit_transform(text)
        model = settings.MODEL
        pred = model.predict(text)
        print(pred)
        return JsonResponse({'prediction': pred})