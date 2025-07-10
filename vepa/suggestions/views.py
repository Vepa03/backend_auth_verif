from django.shortcuts import render
from rest_framework import viewsets
from .models import Suggestion
from .serializer import SuggestionSerializer

class SuggestionView(viewsets.ModelViewSet):
    queryset = Suggestion.objects.all()
    serializer_class = SuggestionSerializer
     