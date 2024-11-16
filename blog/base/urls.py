from django.urls import path

from . import views

urlpatterns = [
    path(route='', view=views.HomeView.as_view(), name='home'),
    path(route='post/<int:pk>/', view=views.PostDetailsView.as_view(), name='post_detail'),
    path(route='add-post/', view=views.AddPostView.as_view(), name='add_post'),
    path(route='update-post/<int:pk>/', view=views.UpdatePostView.as_view(), name='update_post'),
    path(route='delete-post/<int:pk>/', view=views.DeletePostView.as_view(), name='delete_post'),
    path(route='like/<int:pk>/', view=views.LikeView, name='like_post'),
    # path('post/<int:pk>/like/', views.LikeView, name='like_post'),

    path(route='add-category/', view=views.AddCategoryView.as_view(), name='add_category'),
    path(route='add-profile/', view=views.CreateProfilePageView.as_view(), name='add_profile'),
    path(route='category/<str:cats>/', view=views.CategoryView, name='category'),
    path(route='category-list/', view=views.CategoryListView.as_view(), name='category_list'),
    path(route='add-comment/<int:pk>/', view=views.AddCommentView, name='add_comment'),
]