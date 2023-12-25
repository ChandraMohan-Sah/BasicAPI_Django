from django.urls import path, include
from .import views


urlpatterns = [
    path('', views.api_home_get),
    path('post/', views.api_home_post),
    # path('products/', include('products.urls'))
]
