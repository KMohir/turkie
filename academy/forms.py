from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ismingiz'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Elektron pochta'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Telefon raqamingiz'}),
            'message': forms.Textarea(attrs={'placeholder': 'Xabaringizni yozing'}),
        }