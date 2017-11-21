from django.conf.urls import url
from .views import logout, login, register, profile

urlpatterns = [
    url(r'^logout', logout, name="logout"),
    url(r'^login', login, name="login"),
    url(r'^register', register, name="register"),
    url(r'^profile', profile, name="profile")
    ]