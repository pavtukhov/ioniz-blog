from django import forms
from .models import Product

class ContactForm(forms.Form):
	title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Name", "class": "col-lg-6"}))
	email = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder": "E-mail (optional)", "class": "col-lg-6"}))
	website = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder": "Website (optional)", "class": "col-lg-6"}))
	comment = forms.CharField(required=True, widget=forms.Textarea(attrs={"placeholder": "Comment", "class": "col-lg-12"}))
