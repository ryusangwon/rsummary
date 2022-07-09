from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=50, label="제목")
    content = forms.CharField(label="내용", widget=forms.Textarea)
    