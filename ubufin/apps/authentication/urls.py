from django.contrib.auth import auth_views
from .views import logout_view

urlpatterns = [
	path("login", auth_views.LoginView.as_view(), name="login"),
	path("logout", logout_view.as_view(), name="logout"),
]

