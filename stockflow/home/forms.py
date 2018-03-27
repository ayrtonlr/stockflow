from django import forms
from django.contrib.auth.models import User
from .models import Wallet, Company
from django.core.exceptions import ValidationError

class WalletForm(forms.ModelForm):
    def clean_name(self):
        name = self.cleaned_data['name']
        if Wallet.objects.filter(name=name).exists():
            raise forms.ValidationError('The name already exists')
        return name

    companies = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Company.objects.all())
    class Meta:
        model = Wallet
        fields = ( 'name', 'companies')

class EditWalletForm(forms.ModelForm):
    companies = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Company.objects.all())
    class Meta:
        model = Wallet
        fields = ( 'name', 'companies')
