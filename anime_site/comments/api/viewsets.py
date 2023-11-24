from comments.models import Comment
from .serializers import ComentSerializer
from reactions.api.mixins import ReactiondMixin
from rest_framework.viewsets import ReadOnlyModelViewSet
from .mixins import CommentMixin
from rest_framework.permissions import IsAuthenticated


class ComentViewSet(ReactiondMixin, CommentMixin,  ReadOnlyModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = ComentSerializer
    # permission_classes = (IsAuthenticated, )