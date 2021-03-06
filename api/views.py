from classes.models import Classroom
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
)
from .serializers import (
    ClassListSerializer,
    ClassDetailSerializer,
    ClassUpdateSerializer,
    ClassCreateSerializer,
)

class ClassroomListView(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassListSerializer


class ClassroomDetailView(RetrieveAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'


# Complete Me
class ClassroomCreateView(CreateAPIView):
    serializer_class = ClassCreateSerializer

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)

class ClassroomUpdateView(RetrieveUpdateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'


class ClassroomDeleteView(DestroyAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'

# Create your views here.
