from django.urls import path
from blogapp import views

urlpatterns = [
    path('', views.PostView.as_view(), name='post_list'),
    path('accounts/signup/', views.SignUp.as_view(), name='signup'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/newpost/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/editpost/', views.UpdatePostView.as_view(), name='post_edit'),
    path('post/<int:pk>/deletepost/', views.DeletePostView.as_view(), name='post_delete'),
    path('draft-post/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approval, name='comment_approval'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
    path('post/<int:pk>/publish/', views.publish_post, name='publish_post'),

]
