from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import DepositForm
from users.models import UserLibraryAccount
from .models import DepositTransaction,BorrowingTransaction
from django.urls import reverse_lazy
from django.utils import timezone
from books.models import Book
from django.contrib import messages

# Create your views here.

@login_required
def borrow_book(request,pk):
    book = get_object_or_404(Book, pk=pk)
    user_account = request.user.account

    if user_account.balance >= book.borrowing_price:
        BorrowingTransaction.objects.create(
            user=user_account,
            book=book,
            amount=book.borrowing_price
        )

        user_account.balance -= book.borrowing_price
        user_account.save()
        messages.success(request, f"You have successfully borrowed {book.title}.")
        return redirect('profile')
    else:
        messages.error(request,f'User Balance: {user_account.balance} is Insufficient')

    return render(request,'books/details.html',{'book':book})



@login_required
def deposit_view(request):
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            user_account = request.user.account

            DepositTransaction.objects.create(
                user = user_account,
                amount = amount
            )
            user_account.balance += amount
            user_account.save()
            return redirect('profile')
    else:
        form = DepositForm()

    return render(request,'transactions/deposit.html',{'form':form})

@login_required
def return_book(request,transaction_id):
    transaction = get_object_or_404(BorrowingTransaction,id=transaction_id)
    user_account = request.user.account

    if request.method =='POST':
        if not transaction.return_date:
            transaction.return_date = timezone.now()
            transaction.save()

            user_account.balance += transaction.amount
            user_account.save()

            return redirect('profile')
    
    return render(request,'transactions/return.html',{'transaction': transaction})