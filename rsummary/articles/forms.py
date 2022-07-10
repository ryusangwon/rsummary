from xml.dom import ValidationErr
from django import forms
from .models import Article
from .validators import validate_symbols
from django.core.exceptions import ValidationError

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = ['title', 'content'] # __all__
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'title',
                'placeholder': 'Please enter a title'}),
            'content': forms.Textarea(attrs={
                'placeholder': 'Please enter a content'})
            }
        
    def clean_title(self):
        title = self.cleaned_data['title']
        if '*' in title:
            raise ValidationError('No "*"..')
        return title