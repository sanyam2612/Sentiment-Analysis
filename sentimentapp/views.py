from os import name
from django.shortcuts import render

# Create your views here.

from .apps import SentimentappConfig


def home(request):
    return render(request, 'home.html')


def result(request):
    text = request.GET['dummytext']
    vector = SentimentappConfig.vectorizer.transform([text])
    prediction = SentimentappConfig.model.predict(vector)[0]
    return render(request, 'result.html', {'ans': prediction, 'text': text})
