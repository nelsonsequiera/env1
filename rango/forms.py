'''
Created on 29-Nov-2015

@author: nell
'''
from django import forms
from rango.models import category, page, User, UserProfile


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=200, help_text = 'Please enter  category name:')
    views = forms.IntegerField(widget = forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget = forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget = forms.HiddenInput(), required= False)
    
    class Meta:
        model = category
        fields = ('name',) 
        
class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=200, help_text = 'Enter title of the page:')
    url = forms.URLField(max_length=200, help_text = 'Enter URL:')
    views = forms.IntegerField(widget = forms.HiddenInput(), initial=0)
    
    class Meta:
        model = page
        exclude = ('category',)
        
class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password')
        
class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
        
        
        
        
        
        
        
        
        
        
        
        