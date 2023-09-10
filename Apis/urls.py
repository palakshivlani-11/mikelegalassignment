from .views import *
from django.urls import path , include

urlpatterns = [
    path('deactivate/', view = deactivate_subscriber, name='deactivate_subscriber'),
    path('add_subscriber/', view = add_subscriber, name='add_subscriber')
]