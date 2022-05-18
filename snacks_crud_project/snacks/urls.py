from django.urls import path
from .views import (
    HomeView,
    SnackListView,
    SnackDetailView,
    SnackCreateView,
    SnackUpdateView,
    SnackDeleteView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("create/", SnackCreateView.as_view(), name="create"),
    path("<int:pk>", SnackDetailView.as_view(), name="snack_detail"),
    path("update/<int:pk>", SnackUpdateView.as_view(), name="snack_update"),
    path("delete/<int:pk>", SnackDeleteView.as_view(), name="snack_delete"),
]
