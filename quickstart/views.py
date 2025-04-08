from rest_framework import viewsets
from .models import Reporter, Article
from .serializers import ReporterSerializer, ArticleSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class ReporterViewSet(viewsets.ModelViewSet):  # ViewSet for Book model
    queryset = Reporter.objects.all()
    serializer_class = ReporterSerializer

class ArticleViewSet(viewsets.ModelViewSet):  # ViewSet for Book model
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ExampleView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)