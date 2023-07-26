from rest_framework.views import APIView, Request, Response, status
from movies.models import Movie
from movies.serializers import MovieSerializer, MovieOrderSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsEmployeeOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination


class MovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployeeOrReadOnly]

    def get(self, req:Request) -> Response:
        movies = Movie.objects.all()

        result_page = self.paginate_queryset(movies, req)

        serializer = MovieSerializer(instance=result_page, many=True)

        return self.get_paginated_response(serializer.data)
    
    def post(self, req:Request) -> Response:
            serializer = MovieSerializer(data=req.data)

            serializer.is_valid(raise_exception=True)

            serializer.save(user=req.user)
            
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

class MovieDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployeeOrReadOnly]

    def get(self, req:Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)

        serializer = MovieSerializer(instance=movie)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, req:Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)

        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class MovieOrdersView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, req:Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)

        serializer = MovieOrderSerializer(data=req.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(user_ordered=req.user, movie=movie)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)






