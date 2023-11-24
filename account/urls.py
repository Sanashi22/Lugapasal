from django.urls import path
from .views import UserLoginView, UserLogOutAPIView

app_name='account'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/',UserLogOutAPIView.as_view(), name='logout')
]
