from django.urls import path

from bookmarks.views import LoginView

urlpatterns = [
    path('/', LoginView.as_view(), name='index'),
]
