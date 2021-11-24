from django import forms
from django.forms import widgets
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    title = forms.CharField(
        label='Review Title',
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'placeholder': '리뷰 제목을 작성해주세요.'
            }
        )
    )

    content = forms.CharField(
        label='Review Content',
        label_suffix='',
        widget=forms.Textarea(
            attrs={
                'placeholder': '리뷰를 작성해주세요.'
            }
        )
    )

    rank = forms.IntegerField(
        label="Rate",
        label_suffix='',
        widget=forms.NumberInput(
            attrs={
                'placeholder': '★ ~ ★★★★★',
            }
        )
    )

    class Meta:
        model = Review
        exclude = ('user', 'movie', 'like_users',)


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': '댓글을 작성해주세요.'
            }
        )
    )

    class Meta:
        model = Comment
        exclude = ('user', 'review',)