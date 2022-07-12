from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from rarerestapi.views import login_user, register_user
from rarerestapi.views.category import CategoryView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'categories', CategoryView, 'category')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]