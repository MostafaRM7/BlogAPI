from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveAPIView
from rest_framework.viewsets import ModelViewSet

from blog.models import Article
from .permissions import IsStaffOrReadOnly, IsAuthorOrReadOnly, IsSuperUserOrStaffReadOnly
from .serializers import ArticleSerializer, UserSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ['status', 'author']
    search_fields = ['title', 'body', 'author__username', 'author__first_name', 'author__last_name']
    ordering_fields = ['status', 'publish']
    ordering = ['-publish']

    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_classes = [IsAuthorOrReadOnly]
        else:
            permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperUserOrStaffReadOnly]

