from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'), #for naming index or home page
    path('courses/', include('courses.urls', namespace='courses')),
    #namespace is used for a group of urls in courses
]

#checks to see in debug mode and add static files
urlpatterns += staticfiles_urlpatterns() 