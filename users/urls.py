from django.urls import path
from .views import UserRegistrationView,UserLoginView,UserLogout,profile_view

urlpatterns = [
    path('register/', UserRegistrationView.as_view(),name='register'),
    path('login/', UserLoginView.as_view(),name='login'),
    path('logout/', UserLogout,name='logout'),
    path('profile/', profile_view,name='profile'),
]
