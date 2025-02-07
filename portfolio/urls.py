from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from register import views as v

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", v.register, name='register'),
    path("", include("main.urls")),
    path("", include("django.contrib.auth.urls")) 
    # looks for specific folder 'registration' in templates
    # then looks for login.html and auth
    # on login success it goes to /accounts/profile/ | to by pass add LOGIN_REDIRECT_URL='/' to settings.py
    # add additional auth tags to base.html file to restrict view of content on login
    # default logout page at /logout
    # anywhere in the views can use variable request.user to get details of the user
    # ie. request.user.authenticated, request.user.name, request.user.email
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
