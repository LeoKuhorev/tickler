from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import token_blacklist, profile, user_list

urlpatterns = [
    # JWT auth
    path('login', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh',
         jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/blacklist', token_blacklist, name='blacklist'),
    path('profile', profile, name='profile'),
    path('list', user_list, name='list'),
]
