"""Server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework.authtoken import views
from Auth.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    url(r'^auth/', include(router.urls)),
    url('^auth/token/', views.obtain_auth_token),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include('website.urls'))
]

# To obtain a security token:
#   curl -k -H "Content-Type: application/json" -X POST -d '{"username":"[username]","password":"[password]"}' https://byteme.online/auth/token/
# Returns:
#   { 'token' : '9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b' }
# Then make more requests like:
#   curl -k -H 'Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b' -X GET https://byteme.online/auth/user/