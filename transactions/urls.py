from django.urls import path
from . import views

urlpatterns = [
    path('deposit/',views.deposit_view,name='deposit'),
    path('borrow/<int:pk>/',views.borrow_book,name='borrow'),
    path('return/<int:transaction_id>/',views.return_book,name='return'),
]