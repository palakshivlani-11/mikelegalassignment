from rest_framework import serializers
from emailcampaigns.models import EmailCampaign

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailCampaign
        fields = "__all__"