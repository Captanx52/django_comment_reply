from django.shortcuts import render
from .models import Post, Comment, CommentAnswer

def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post=post)
    answers = CommentAnswer.objects.filter(comment__post=post)
    context = {'post': post, 'comments': comments, 'answers': answers}
    return render(request, 'Post/post_detail.html', context)