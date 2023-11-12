from .views import RegisterAPI
from django.urls import path
from knox import views as knox_views
from .views import LoginAPI,profile
from django.urls import path
from .views import LogoutView

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),

]