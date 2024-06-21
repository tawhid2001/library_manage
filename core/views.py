from django.shortcuts import render
from django.views.generic import TemplateView
from books.models import Book
from categories.models import Category
from django.shortcuts import get_object_or_404

# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs.get('category_slug')

        if category_slug:
            cat = get_object_or_404(Category,slug=category_slug)
            context['data'] = Book.objects.filter(category = cat)
        else:
            context['data'] = Book.objects.all()

        context['category'] = Category.objects.all()

        return context