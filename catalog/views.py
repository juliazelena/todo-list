from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from catalog.models import Post, Tag


def index(request: HttpRequest) -> HttpResponse:
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "post_list": post_list,
        "page_obj": page_obj,
    }
    return render(request, "catalog/index.html", context=context)


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5
