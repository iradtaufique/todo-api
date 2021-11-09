from django.urls import path
from authentication.views import AuthUserAPIView, LoginAPIView, RegisterApiView

urlpatterns = [
    path('register/', RegisterApiView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('user/', AuthUserAPIView.as_view(), name='user'),

]
