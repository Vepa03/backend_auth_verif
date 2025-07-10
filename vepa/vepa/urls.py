"""
URL configuration for vepa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts.views import *
from rest_framework import routers
from category.views import CategoryView
from book.views import BookView
from suggestions.views import SuggestionView
from django.conf.urls.static import static

router = routers.DefaultRouter()

router.register('category', CategoryView, basename='category')
router.register('books', BookView, basename='books')
router.register('suggestions', SuggestionView, basename='suggestions' )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterAPI.as_view()),
    path('verify/', VerifyOTP.as_view()),
    path('login/', Login.as_view()),
    path('api/', include(router.urls))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
