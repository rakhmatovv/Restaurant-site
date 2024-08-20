from django import forms
from .models import *


class BookTableForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg custom-form-control',
        'type': 'text',
        'placeholder': 'Enter your name...'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg custom-form-control',
        'type': 'text',
        'placeholder': 'Enter your last name...'
    }))
    phone = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg custom-form-control',
        'type': 'number',
        'placeholder': 'Write your number...'
    }))
    spending_time = forms.ChoiceField(choices=SPENDING_TIME,
                                      required=True,
                                      label='Rate product from 1 to 5',
                                      widget=forms.Select(attrs={
                                          'class': 'form-control form-control-lg custom-form-control'}), )
    party = forms.ChoiceField(choices=PARTY,
                              required=True,
                              label='Rate product from 1 to 5',
                              widget=forms.Select(attrs={
                                  'class': 'form-control form-control-lg custom-form-control'}), )
    table = forms.ChoiceField(choices=TABLE,
                              required=True,
                              label='Rate product from 1 to 5',
                              widget=forms.Select(attrs={
                                  'class': 'form-control form-control-lg custom-form-control'}), )
    time = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg custom-form-control',
        'type': 'time'
    }))
    date = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg custom-form-control',
        'type': 'date'
    }))

    class Meta:
        model = BookTable
        fields = (
        'name', 'last_name', 'phone', 'spending_time', 'party', 'table', 'time',
        'date')
