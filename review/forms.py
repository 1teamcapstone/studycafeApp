from django import forms
from .models import Review

class ReviewForm(forms.Form):
    contents = forms.CharField(error_messages = {'required':"내용을 입력해주세요."}, label = "내용", widget = forms.Textarea)
    
