from django.contrib import admin
from app.models import UserProfileInfo,User,Document
from social.apps.django_app.default.models import UserSocialAuth

# Register your models here.

admin.site.register(UserProfileInfo)
admin.site.register(Document)
