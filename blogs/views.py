from django.shortcuts import get_object_or_404, render
from .models import Category, Blog


def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status="Published", category=category_id)
    category = get_object_or_404(Category, id=category_id)
    context = {"posts": posts, "category": category}
    return render(request, "posts_by_category.html", context)
