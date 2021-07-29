from django.contrib import admin
from basic_app.models import Question,Choice,UserProfileInfo
# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(UserProfileInfo)
