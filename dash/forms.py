from django import forms

from gov.models import Post, Category

class SendForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['coursecategory', 'coursename', 'email', 'banner']


class CategorySendForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('coursecategory', 'email')
        
