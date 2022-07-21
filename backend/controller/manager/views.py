from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Manager
from .serializers import ManagerSerializer

class ManagerListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    pagination_class = None

class ManagerView(RetrieveAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

class TopSellerView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Manager.objects.filter(top_seller=True)
    serializer_class = ManagerSerializer
    pagination_class = None