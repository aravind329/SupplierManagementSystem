from django.urls import path
from .views import ManagerListView, ManagerView, TopSellerView

urlpatterns = [
    path('', ManagerListView.as_view()),
    path('topseller', TopSellerView.as_view()),
    path('<pk>', ManagerView.as_view()),
]