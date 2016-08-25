from django.conf.urls import url

from .views import MovieListView

app_name = "movies"
urlpatterns = [
	url(r'^', MovieListView.as_view(), name="movies_list")
]