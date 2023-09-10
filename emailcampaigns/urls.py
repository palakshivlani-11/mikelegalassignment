from django.urls import path
from emailcampaigns.views import *

urlpatterns = [
    path('campaign/',  view = campaign, name='campaign'),
]