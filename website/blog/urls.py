from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('news/', news, name='news'),
    path('settlement/', settlement, name='settlement'),
    path('regulations/', regulations, name='regulations'),
    path('decisions/', decisions, name='decisions'),
    path('resolutions/', resolutions, name='resolutions'),
    path('self_government/', self_government, name='self_government'),
    path('municipal_control/', municipal_control, name='municipal_control'),
    path('prosecutors_info/', prosecutors_info, name='prosecutors_info'),
    path('rossreestr_info/', rossreestr_info, name='rossreestr_info'),
    path('rossreestr_info/', rossreestr_info, name='rossreestr_info'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
]
