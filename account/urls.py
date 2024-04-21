from django.urls import path, include
from .views import activate_account

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # path('activate/<str:uidb64>/<str:token>/', activate_account, name='activate_account'),
]
