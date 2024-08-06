from django.urls import path
from . import views
from .views import SignUpView

urlpatterns = [
    path('', views.list_yarn, name="all_yarn"),
    path('<int:yarn_id>/', views.display_yarn, name="yarn"),
    path("signup/", SignUpView.as_view(), name="signup")
]
