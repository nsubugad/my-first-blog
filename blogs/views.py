from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
	posts = Post.objects.filter(publised_date__lte=timezone.now()).order_by('publised_date__lte')
	return render(request, 'blogs/post_list.html',{'posts': posts})