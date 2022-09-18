from django import forms

from news_act.models import Category, News
import re
from django.core.exceptions import ValidationError


# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150, label='Название', widget=forms.TextInput(attrs={'class': 'form-control'}))
#     content = forms.CharField(label='Ваш текст', required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
#     is_pub = forms.BooleanField(label='Опубликована', initial=True)
#     category = forms.ModelChoiceField(empty_label='Выбирите категорию...', label='Категория', queryset=Category.objects.all(), widget=forms.Select(
#         attrs={'class': 'form-control'}
#     ))

class NewsForm(forms.ModelForm):
    error_css_class = "error"

    class Meta:
        model = News
        # fields = "__all__"

        fields = ['title', 'content', 'is_pub', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title

    # def clean_is_pub(self):
    #     is_pub = self.cleaned_data['is_pub']
