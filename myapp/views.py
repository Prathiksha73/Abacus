from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class TestProtectedAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "message": "JWT authentication successful",
            "user": request.user.username
        })
#CREATE YOUR VIEW HERE