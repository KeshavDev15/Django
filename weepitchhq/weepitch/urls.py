from django.urls import path
from . import views
urlpatterns = [
    path("", views.weepitch_list, name="weepitch_list"),
    path("create/", views.weepitch_create, name="weepitch_create"),
    path("<int:weepitch_id>/edit/", views.weepitch_edit, name="weepitch_edit"),
    path("<int:weepitch_id>/delete/", views.weepitch_delete, name="weepitch_delete"),
    path("/register/", views.register, name="register"),
    #path("/login/", views.login, name="login"),
]
