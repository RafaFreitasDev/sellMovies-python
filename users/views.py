from rest_framework.views import APIView, Request, Response, status
from users.models import User
from users.serializers import UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsUserOwner

class UserView(APIView):
    def get(self, req:Request) -> Response:
        users = User.objects.all()

        serializer = UserSerializer(instance=users, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def post(self, req:Request) -> Response:
            serializer = UserSerializer(data=req.data)

            serializer.is_valid(raise_exception=True)

            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsUserOwner]

    def get(self, req:Request, user_id:int) -> Response:
        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(req, user)

        serializer = UserSerializer(instance=user)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, req:Request, user_id:int) -> Response:
            user = get_object_or_404(User, id=user_id)
            self.check_object_permissions(req, user)

            serializer = UserSerializer(instance=user, data=req.data, partial=True)

            serializer.is_valid(raise_exception=True)

            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)    
     


        
       
            
        
    
        
