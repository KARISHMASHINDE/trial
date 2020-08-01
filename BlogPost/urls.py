from django.urls import path
from django.conf.urls import url
from BlogPost import views
from .views import registration_view, PostLikeAPIToggle
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token



urlpatterns = [
    path('list/', views.PoststList.as_view()),
    path('details/<int:pk>/', views.PostsDetail.as_view()),
    url(r'api/^(?P<slug>[\w-]+)/claps/$', PostLikeAPIToggle,name="claps-api-toggle"),
    path('api/register/',registration_view),
    url(r'^api-token/', obtain_jwt_token),
    url(r'^token-refresh/', refresh_jwt_token),
    
]