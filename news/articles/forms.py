from django import forms
from .models import Comment, Star

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ( "comment", )

class RatingForm(forms.ModelForm):
    RATING_CHOICES = (
        (1, ''),
        (2, ''),
        (3, ''),
        (4, ''),
        (5, ''),
    )
    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect)
    class Meta:
        model = Star
        fields = ("rating", )