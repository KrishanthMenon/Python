from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from hi.views import HelloWorldView
from hi.views import Postview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello', HelloWorldView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]

router = routers.SimpleRouter()
router.register('post', Postview)
urlpatterns += router.urls
