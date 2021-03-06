from django.urls import path, re_path, include
from . import views
from django.test import SimpleTestCase, override_settings

urlpatterns = [
	path('', views.index, name='index'),
	path('about/', views.about_us, name = 'about_us'),
	path('<int:pk>/', views.profile, name = 'profile'),
	path('posts/new', views.post_create, name = 'post_create'),
	path('posts/<int:pk>', views.post_detail, name = 'post_detail'),
	path('posts/<int:pk>/edit', views.post_edit, name = 'post_edit'),
	path('posts/<int:pk>/delete', views.post_delete, name = 'post_delete'),
	path('posts/<int:pk>/comments', views.comment_create, name = 'comment_create'),
	path('comments/', views.comment_list, name = 'comment_list'),
	path('comments/<int:pk>', views.comment_detail, name = 'comment_detail'),
	path('comments/<int:pk>/edit', views.comment_edit, name = 'comment_edit'),
	path('comments/<int:pk>/delete', views.comment_delete, name = 'comment_delete'),
	re_path(r'^search/', include([
		re_path(r'^$', views.global_view, name="global_view"),
		path('?q=<str:query>', views.global_view, name="global_view"),
	])),
	path('like_post/<int:post_id>/', views.like_post, name="like_post"),
	path('follow_user/<int:f_user_id>/', views.follow_user, name="follow_user"),
	path('get_followers/<int:pk>/', views.get_followers, name="get_followers"),
]