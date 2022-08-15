from django.urls import path

from .views import SnackListCreateView, SnackDetailView
urlpatterns = [
    path('', SnackListCreateView.as_view(), name='snack_list_create'),
    path('<int:pk>/', SnackDetailView.as_view(), name='snack_detail'),
]