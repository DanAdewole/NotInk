from django.urls import path

# from .views import SignUpView
from .views import sign_up_view


urlpatterns = [
	path('signup/', sign_up_view, name='signup')
]
