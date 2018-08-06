from django.conf.urls import url, include
from rest_framework.schemas import get_schema_view
from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path

schema_view = get_schema_view(title='Mosaic API')

urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^', include('music.urls')),
    path('token-auth/', obtain_jwt_token)
]
