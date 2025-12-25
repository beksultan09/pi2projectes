from django.urls import path, include
from .views import (UserProfileListAPIView, UserProfileDetailAPIView, CategoryListAPIView, CategoryDetailAPIView,
                    GenreListAPIView, GenreDetailAPIView,
                    CountryListAPIView,CountryDetailAPIView, DirectorListAPIView,
                    DirectorDetailAPIView, ActorListAPIView, ActorDetailAPIView,
                    MovieListAPIView, MovieDetailAPIView,
                    RatingViewSet, ReviewViewSet, ReviewLikeViewSet,
                    FavoriteViewSet, FavoriteItemViewSet, HistoryViewSet)
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'rating', RatingViewSet)
router.register(r'review_like', ReviewLikeViewSet)
router.register(r'favorite', FavoriteViewSet)
router.register(r'favorite_items', FavoriteItemViewSet)
router.register(r'history', HistoryViewSet)
router.register(r'review', ReviewViewSet)




urlpatterns = [
    path('', include(router.urls)),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('genre/', GenreListAPIView.as_view(), name='genre_list'),
    path('genre/<int:pk>/', GenreDetailAPIView.as_view(), name='genre_detail'),
    path('movie/', MovieListAPIView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailAPIView.as_view(), name='movie_detail'),
    path('country/', CountryListAPIView.as_view(), name='country_detail'),
    path('country/<int:pk>/', CountryDetailAPIView.as_view(), name='country_list'),
    path('director/', DirectorListAPIView.as_view(), name='director_list'),
    path('director/<int:pk>/', DirectorDetailAPIView.as_view(), name='director_detail'),
    path('actor/', ActorListAPIView.as_view(), name='actor_list'),
    path('actor/<int:pk>/', ActorDetailAPIView.as_view(), name='actor_detail'),
    path('user/', UserProfileListAPIView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail'),
]