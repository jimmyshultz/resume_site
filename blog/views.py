from django.shortcuts import render, redirect

from .models import BlogPost, Comment, Category
from .forms import CommentForm

def blog_homepage(request):
    categories = Category.objects.all()
    blogposts = BlogPost.objects.all()
    comments = Comment.objects.all()
    context = {'categories': categories, 'blogposts': blogposts, 'comments': comments,}
    return render(request, 'blog/blog.html', context)

def category(request, category_id):
    """Show all posts under a single category."""
    category = Category.objects.get(id=category_id)
    categories = Category.objects.all()
    context = {'category': category, 'categories': categories}
    return render(request, 'blog/category.html', context)

def blogpost(request, blogpost_id):
    """Show a single blog post and its comments."""
    blogpost = BlogPost.objects.get(id=blogpost_id)
    comments = blogpost.comment_set.order_by('date_added')
    categories = Category.objects.all()
    context = {'blogpost': blogpost, 'comments': comments, 'categories': categories}
    return render(request, 'blog/blog_post.html', context)

def new_comment(request, blogpost_id):
    """A form to add a new comment to a blog post."""
    blogpost = BlogPost.objects.get(id=blogpost_id)
    categories = Category.objects.all()

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = CommentForm()
    else:
        # POST data submitted; process data.
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.blogpost = blogpost
            new_comment.save()
            return redirect('blog:blogpost', blogpost_id=blogpost_id)
    
    #Display a blank or invalid form.
    context = {'blogpost': blogpost, 'categories': categories, 'form': form}
    return render(request, 'blog/new_comment.html', context)