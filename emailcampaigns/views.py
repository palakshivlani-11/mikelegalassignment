from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from emailcampaigns.serializers import CampaignSerializer
from emailcampaigns.emailsender import send_emails
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['POST'])
def campaign(request):
    
    try:
        serializer = CampaignSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            send_emails(campaign=serializer.data)
            return Response(
                {"data": serializer.data, "message": "Campaign Created Successfully"}, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(str(e) , status=status.HTTP_400_BAD_REQUEST)