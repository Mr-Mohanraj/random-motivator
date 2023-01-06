from django.urls import path
from loginsystem.views import RegisterApiView, LoginApiView, ResetAPIView, UserApiView, RefreshAPIVew, ResetAPIView, ForgetAPIView

# as_view() indicate the view is a class view
urlpatterns = [
    path('register', RegisterApiView.as_view()),
    path('login', LoginApiView.as_view()),
    path('user', UserApiView.as_view()),
    path('refresh', RefreshAPIVew.as_view()),
    path('reset', ResetAPIView.as_view()),
    path('forgot', ForgetAPIView.as_view())
]
