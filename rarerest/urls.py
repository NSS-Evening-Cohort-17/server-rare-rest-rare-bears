from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from rarerestapi.views import login_user, register_user, PostView
from rarerestapi.views.category import CategoryView
from rarerestapi.views.tag import TagView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'categories', CategoryView, 'category')
router.register(r'posts', PostView, 'post')
router.register(r'tags', TagView, 'tag')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]