from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'Cindy Nduku',
        'title': 'My First Post',
        'content': 'First Post Content',
        'date_posted': 'October,28,2020'
    },
     {
        'author': 'Valerie Gaya',
        'title': 'My Second Post',
        'content': 'Second Post Content',
        'date_posted': 'October,29,2020'
    },
]
# Create your views here.
def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})    