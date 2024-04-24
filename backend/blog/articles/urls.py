from django.urls import path

from .views import *

urlpatterns=[
    path("<int:pk>/", ArticleDetailView.as_view()),
    path("<int:pk>/update/", ArticleUpdateView.as_view()),
    # path("<int:pk>/delete/", ArticleDeleteView.as_view()),
    path("", ArticleListCreateView.as_view())
]