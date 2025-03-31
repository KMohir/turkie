from django.shortcuts import render, redirect
from django.contrib import messages
from .models import News
from .forms import ContactForm
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

# Главная страница
from django.shortcuts import render
from .models import News

from django.shortcuts import render, get_object_or_404
from .models import News

from django.shortcuts import render, get_object_or_404
from .models import News


from django.shortcuts import render, get_object_or_404
from .models import News
def home(request):
    news_items = News.objects.all()[:4]  # Get the latest 4 news items
    return render(request, 'academy/home.html', {'news_items': news_items})

def news_list(request):
    news_items = News.objects.all()
    return render(request, 'academy/news_list.html', {'news_items': news_items})



def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    news.views_count += 1  # Увеличиваем счётчик просмотров
    news.save()
    return render(request, 'academy/news_detail.html', {'news': news})
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем сообщение в базе данных
            messages.success(request, 'Xabaringiz muvaffaqiyatli yuborildi!')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'academy/contact.html', {'form': form})


# Детальная страница новости
