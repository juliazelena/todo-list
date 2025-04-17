from django.urls import path

from catalog.views import (
    index,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    PostCreateView,
    # toggle_task_status,
    # PostUpdateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("/create/", PostCreateView.as_view(), name="post-create"),
    # path('post/<int:pk>/toggle/', toggle_task_status,
    #      name='toggle-task-status'),
    # path("/<int:pk>/update/", PostUpdateView.as_view(), name="post-update")
]

app_name = "catalog"
