from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from catalog.models import Post, Tag


def index(request: HttpRequest) -> HttpResponse:
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "paginator": paginator,
        "page_obj": page_obj,
    }
    return render(request, "catalog/index.html", context=context)


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5
    

class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("catalog:tag-list")
    template_name = "catalog/tag_form.html"
    

class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("catalog:tag-list")
    template_name = "catalog/tag_form.html"
    
    
class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("catalog:tag-list")
    template_name = "catalog/tag_confirm_delete.html"


class PostCreateView(generic.CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("catalog:index")
    template_name = "catalog/post_form.html"


def toggle_post_status(request: HttpRequest, pk: int) -> HttpRequest:
    post = get_object_or_404(Post, pk=pk)
    post.is_done = not post.is_done
    post.save()
    return redirect("catalog:index")


class PostUpdateView(generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("catalog:index")
    template_name = "catalog/post_form.html"


class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy("catalog:index")
    template_name = "catalog/post_confirm_delete.html"


