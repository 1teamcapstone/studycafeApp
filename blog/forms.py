from django import forms
from .models import Post
from django.forms.widgets import NumberInput

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'study_place', 'study_day','start_date', 'end_date','start_time', 'end_time', 'limit_people')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'study_place': forms.TextInput(attrs={'class': 'form-control'}),
            'study_day': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '매주 무슨 요일'}),
            'start_date': forms.NumberInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.NumberInput(attrs={'type': 'date', 'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'end_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'limit_people': forms.NumberInput(attrs={'step': 1, 'max': 10, 'min': 2, 'class': 'form-control'}),                            
        }
        labels = {
            'title': '스터디명',
            'study_place': '스터디장소',
            'study_day': '스터디요일',
            'start_date': '시작일자', 
            'end_date': '종료일자',
            'start_time': '시작시각', 
            'end_time': '종료시각', 
            'limit_people': '제한인원',
        }  