from django.urls import path
from . import views

urlpatterns = [
    path('details/<int:pk>/',views.DetailsBookView.as_view(),name='details'),
]