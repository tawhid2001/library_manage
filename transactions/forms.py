from django import forms 
from .models import DepositTransaction,BorrowingTransaction

class BorrowForm(forms.ModelForm):
    class Meta:
        model = BorrowingTransaction
        fields = ['book']

        

class DepositForm(forms.ModelForm):
    class Meta:
        model = DepositTransaction
        fields = ['amount']

    def clean_amount(self):
        min_deposit_amount = 100
        amount = self.cleaned_data.get('amount')
        if amount < min_deposit_amount:
            raise forms.ValidationError(
                f'You neet to deposit at least {min_deposit_amount}$'
            )
        
        return amount