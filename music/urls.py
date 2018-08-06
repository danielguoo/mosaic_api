from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from music import views
from django.urls import path

urlpatterns = [
    url(r'^albums/$', views.AlbumList.as_view()),
    url(r'^albums/(?P<pk>[0-9]+)/$', views.AlbumDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    path('current_user/', views.current_user),
    url(r'^reviews/$', views.ReviewList.as_view()),
    url(r'^reviews/(?P<pk>[0-9]+)/$', views.ReviewDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
