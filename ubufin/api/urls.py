from django.urls import path, include

urlpatterns = [
	path("users/", include("ubufin.api.authentication.urls"))
]