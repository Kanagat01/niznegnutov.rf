from django.views.generic import DetailView
from django.shortcuts import redirect, render
from .models import *
from .forms import *


def home(request):
    reception_form = ReceptionForm()
    message_form = MessageForm()
    context = {
        'reception_form': reception_form,
        'message_form': message_form
    }

    if request.method == 'POST':
        if request.method == 'POST':
            if request.POST.get('content'):
                form = MessageForm(request.POST)
                if form.is_valid():
                    content = form.cleaned_data['content']
                    Suggestion.objects.create(content=content)
                    return redirect('home')
            elif request.POST.get('question'):
                form = ReceptionForm(request.POST)
                if form.is_valid():
                    name = form.cleaned_data['name']
                    email = form.cleaned_data['email']
                    phone_number = form.cleaned_data['phone_number']
                    question = form.cleaned_data['question']
                    Reception.objects.create(name=name, email=email, phone_number=phone_number, question=question)
                    return redirect('home')
            else:
                return render(request, 'blog/home.html', context)

    return render(request, 'blog/home.html', context)


def news(request):
    context = {
        'title': 'Новости',
        'articles': Article.objects.filter(cat=Category.objects.get(name='Новости').pk)
    }
    return render(request, 'blog/articles.html', context)


def settlement(request):
    context = {
        'title': 'Поселение',
        'articles': Article.objects.filter(cat=Category.objects.get(name='Поселение').pk)
    }
    return render(request, 'blog/articles.html', context)


def regulations(request):
    context = {
        'title': 'Регламенты',
        'articles': Article.objects.filter(cat=Category.objects.get(name='Регламенты').pk)
    }
    return render(request, 'blog/articles.html', context)


def decisions(request):
    context = {
        'title': 'Решения',
        'articles': Article.objects.filter(cat=Category.objects.get(name='Решения').pk)
    }
    return render(request, 'blog/articles.html', context)


def resolutions(request):
    context = {
        'title': 'Постановления',
        'articles': Article.objects.filter(cat=Category.objects.get(name='Постановления').pk)
    }
    return render(request, 'blog/articles.html', context)


def self_government(request):
    context = {
        'title': 'Полномочия органов местного самоуправления',
        'articles': Article.objects.filter(cat=Category.objects.get(name='Полномочия органов местного самоуправления').pk)
    }
    return render(request, 'blog/articles.html', context)


def municipal_control(request):
    context = {
        'title': 'Муниципальный контроль',
        'articles': Article.objects.filter(cat=Category.objects.get(name='Муниципальный контроль').pk)
    }
    return render(request, 'blog/articles.html', context)


def prosecutors_info(request):
    context = {
        'title': 'Информация Прокуратуры',
        'articles': Article.objects.filter(cat=Category.objects.get(name='Информация Прокуратуры').pk)
    }
    return render(request, 'blog/articles.html', context)


def rossreestr_info(request):
    context = {
        'title': 'Информация Россреестра',
        'articles': Article.objects.filter(cat=Category.objects.get(name='Информация Россреестра').pk)
    }
    return render(request, 'blog/articles.html', context)


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'