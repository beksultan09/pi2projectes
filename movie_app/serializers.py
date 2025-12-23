from .models import (UserProfile, Category, Genre, Country, Director, Actor,
                    Movie, MovieVideo, MovieFrame, Rating, Review, ReviewLike,
                    Favorite, FavoriteItem, History)
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class UserProfileReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'user_photo']


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class GenreNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre_name']


class CategoryDetailSerializer(serializers.ModelSerializer):
    genres = GenreNameSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['category_name', 'genres']


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'genre_name']



class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'country_name']




class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['full_name']


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['full_name']


class MovieListSerializer(serializers.ModelSerializer):
    year = serializers.DateField(format('%Y'))
    country = CountryListSerializer(many=True)
    genre = GenreNameSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'movie_poster', 'movie_name',
                  'year', 'country', 'genre', 'movie_status']


class GenreDetailSerializer(serializers.ModelSerializer):
    genres_movies = MovieListSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = ['genre_name', 'genres_movies']


class MovieVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieVideo
        fields = ['video_name', 'video']


class MovieFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieFrame
        fields = ['image']


class RatingSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M')
    user = UserProfileReviewSerializer()
    class Meta:
        model = Rating
        fields = ['user', 'stars', 'created_date']


class ReviewSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    class Meta:
        model = Review
        fields = ['user', 'comment', 'created_date']


class MovieDetailSerializer(serializers.ModelSerializer):
    year = serializers.DateField('%d-%m-%Y')
    country = CountryListSerializer(many=True)
    director = DirectorSerializer(many=True)
    genre = GenreNameSerializer(many=True)
    actor = ActorSerializer(many=True)
    videos = MovieVideoSerializer(many=True, read_only=True)
    frames = MovieFrameSerializer(many=True, read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['movie_name', 'year', 'slogan', 'country', 'director', 'genre',
                  'movie_type', 'movie_time', 'actor', 'movie_poster', 'trailer',
                  'description', 'movie_status', 'videos', 'frames', 'ratings',
                  'reviews']


class ReviewLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewLike
        fields = '__all__'


class CountryDetailSerializer(serializers.ModelSerializer):
    countries = MovieListSerializer(many=True, read_only=True)
    class Meta:
        model = Country
        fields = ['country_name', 'countries']


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class FavoriteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItem
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'