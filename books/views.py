from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Book
from . import forms
from django.views.generic import DetailView

# Create your views here.

class DetailsBookView(DetailView):
    model = Book
    template_name = 'books/details.html'
    

    def post(self,request,*args,**kwargs):
        self.object = self.get_object()
        review_form = forms.ReviewForm(data=self.request.POST)
        user = self.request.user
        book = self.get_object()
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.book = book
            new_review.user = user
            new_review.save()
            return redirect(reverse('details', kwargs={'id': book.id}))
        return self.get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        book = self.object
        reviews = book.reviews.all()
        review_form = forms.ReviewForm()
        
        context['reviews'] = reviews
        context['review_form'] = review_form
        return context
    
    