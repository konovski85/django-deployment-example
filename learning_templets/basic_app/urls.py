from django.urls import path
from basic_app import views

#Template tagging
app_name = "basic_app"


urlpatterns = [
    path("relative/", views.relative, name = "relative"),
    path("other/", views.other, name = 'other'),
    path("registration/", views.register, name = "register"),
    path('user_login/', views.user_login, name = 'user_login'),
]
