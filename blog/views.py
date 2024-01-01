from django.shortcuts import render

posts = [
    {
        'author': 'Corey Delamingas',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date posted': 'December 30, 2023',
    },
    
    {
        'author': 'Ding-dong',
        'title': 'Blog Post 2',
        'content': 'Is video game good',
        'date posted': 'December 30, 2023',
    }
]

def home (request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})