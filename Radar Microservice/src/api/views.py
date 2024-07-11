from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import AttackSerializer
from rest_framework import status

@api_view(["POST"])
def attack_detected(request):
    try:

        # Get json data from request body:
        json = request.data
        serializer = AttackSerializer(data = json)
        
        # Validate: 
        if not serializer.is_valid():
            json = { "error": serializer.errors }
            return Response(json, status = status.HTTP_400_BAD_REQUEST)

        # Save to database: 
        serializer.save()

        # Response back:
        return Response(serializer.data, status = status.HTTP_201_CREATED)
        
    except Exception as err:
        json = { "error": str(err)}
        return Response(json, status = status.HTTP_500_INTERNAL_SERVER_ERROR)