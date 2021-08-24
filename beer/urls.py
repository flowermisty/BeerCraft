from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index ,name = 'index'),
    path('ver1', views.ver1, name = 'ver1'),
    path('ver2', views.ver2, name = 'ver2'),
    path('ver3', views.ver3, name = 'ver3'),
    path('ver4', views.ver4, name = 'ver4'),
    # path('detail', views.detail, name = 'detail'),
    path('detail/review_create/<int:DetailInfo_id>', views.review_create, name='review_create'),
    path('common/', include('common.urls')),
    path('detail/<int:DetailInfo_id>', views.detail, name = 'detail'),
    path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('answer/modify/<int:comment_id>/', views.comment_modify, name='comment_modify'),

    path('comment/create/answer/<int:answer_id>/', views.comment_create_answer, name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/', views.comment_modify_answer, name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/', views.comment_delete_answer, name='comment_delete_answer'),
    path('vote/answer/<int:answer_id>/', views.vote_answer, name='vote_answer'),
]
