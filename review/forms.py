from django import forms
from .models import Review

class ReviewForm(forms.Form):    
    #sca_name = forms.CharField(error_messages = {'required':"스터디카페 이름을 입력해주세요."}, label = "스터디카페", max_length=128)
    contents = forms.CharField(error_messages = {'required':"내용을 입력해주세요."}, label = "내용", widget = forms.Textarea)
    
