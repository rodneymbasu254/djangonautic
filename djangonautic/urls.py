from django.contrib import admin
from django.urls import path,include
from.import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('article/',include('articles.urls')),
    path('about/',views.about),
    path('',views.homepage),
]
