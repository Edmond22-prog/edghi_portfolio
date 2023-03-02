from django.urls import path
from .views import HomeView, CaseView


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('details/<str:pk>/<slug:project>/', CaseView.as_view(), name="case"),
]
