from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', HomeAds.as_view(), name='home'),
    path('category/<int:category_id>/', AdsByCategory.as_view(), name='category'),
    path('ads/<int:pk>/', ViewAds.as_view(), name='view_ads'),
    path('ads/add_ads/', CreateAds.as_view(), name='add_ads'),
]
