from django import forms

class blog_form(forms.Form):
    title=forms.CharField(label='Title',max_length=20,widget= forms.TextInput(attrs={'class':'form-control'}))
    data=forms.CharField(max_length=200,widget= forms.Textarea(attrs={'class':'editable'}))
    author=forms.CharField(label='author',max_length=10,widget= forms.TextInput(attrs={'class':'form-control'}))

