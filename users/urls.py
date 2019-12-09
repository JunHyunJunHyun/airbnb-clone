from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("login", views.LogInView.as_view(), name="login"),
    path("logout", views.log_out, name="logout"),
    path("signup", views.SignUpView.as_view(), name="signup"),
    path("verify/<str:key>", views.complete_verificaton, name="complete-verificaton"),
]

