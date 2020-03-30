from django import forms
from candidate_profile.models import UserProfileInfo, Document
from social.apps.django_app.default.models import UserSocialAuth

from django.contrib.auth.models import User

class DocumentForm(forms.ModelForm):
    class Meta():
        model = Document
        fields = ('__all__')