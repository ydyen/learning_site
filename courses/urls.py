from django.urls import path
from . import views

#variable for url path in base directory
app_name = 'courses'

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<pk>', views.course_detail, name="detail"),
    path('<course_pk>/<step_pk>', views.step_detail, name='step'),
]
