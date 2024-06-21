from django.contrib import admin
from .models import BorrowingTransaction,DepositTransaction

# Register your models here.

admin.site.register(BorrowingTransaction)
admin.site.register(DepositTransaction)