from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from rarerestapi.views import login_user, register_user, PostView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'posts', PostView, 'post')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]