from django.urls import path
from .views import *


urlpatterns = [
    path('signin/', signin),
    path('detect', dectect_list),
    path('camera', camera),
    path('date_filter/', date_filter),
    path('mydate_filter/', mydate_filter),
    #  path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),

]