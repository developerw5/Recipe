"""RecipeProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from recipe.views import RecipeCategoryAPIView, ProductCategoryApiView, RecipeApiView, ProductApiView,IngredientApiView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/recipecategories/', RecipeCategoryAPIView.as_view()),
    path('api/v1/recipes/', RecipeApiView.as_view()),
    path('api/v1/recipes/<int:pk>/', RecipeApiView.as_view()),
    path('api/v1/productcategories/', ProductCategoryApiView.as_view()),
    path('api/v1/products/', ProductApiView.as_view()),
    path('api/v1/products/<int:pk>/', ProductApiView.as_view()),
    path('api/v1/ingredient/', IngredientApiView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
