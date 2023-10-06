from django.urls import path
from .views import *
from workwave.apps.users.api.views import RegisterUserView, LoginUserView, LogoutUserView, UserDetailView, UploadImageView, ChangePasswordView, UserViewSet

urlpatterns = [
    path("register/", view=RegisterUserView.as_view(), name="register"),
    path("login/", view=LoginUserView.as_view(), name="login"),
    path("logout/", view=LogoutUserView.as_view(), name="logout"),
    path("users/list", view=UserViewSet.as_view({'get': 'list'}), name="users_list"),
    path("user/detail/<int:pk>", view=UserDetailView.as_view(), name="user_detail"),
    path("user/update/<int:pk>", view=UserDetailView.as_view(), name="user_update"),
    path("user/update/password/<int:pk>", view=ChangePasswordView.as_view(), name="change_password"),
    path("user/delete/<int:pk>", view=UserDetailView.as_view(), name="user_delete"),
    path("user/image/<int:pk>", view=UploadImageView.as_view(), name="user_avatar"),
]
