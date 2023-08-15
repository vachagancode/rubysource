from django.urls import path, re_path
from django.conf.urls.static import static

from django.conf import settings
from . import views
from django.views.static import serve

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('new_course/', views.new_course, name='course'),
    path('courses/<str:parameter>/', views.category_check, name='category'),
    path('courses/<str:parameter>/<int:course_id>/', views.course_check, name='courses_of_cat'),
    path('new_resource/', views.new_resource, name='resource'),
    path('new_copyright_rule/', views.new_copyright, name='copyright'),
    path('new_category/', views.new_category, name='new_category'),
    path('new_course_of_category/', views.new_category_course, name='new_cat_course'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)