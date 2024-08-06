from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignUpForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = (
            "first_name", "username", "password1", "password2"
        )


class ReviewForm(forms.Form):
    
    # declare our own review form with only a field for content because we
    # determine and save their details/the yarn it refers to programmatically
    review_content = forms.CharField(
        label="Tell us what you think",
        widget=forms.Textarea
    )
