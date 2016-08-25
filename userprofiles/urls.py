from django.conf.urls import url 

from .views import UserCreateView

app_name = "user"
urlpatterns = [
	url(r'^create/', UserCreateView.as_view(), name="user_create"),
]