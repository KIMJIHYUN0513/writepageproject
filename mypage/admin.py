from django.contrib import admin
from .models import Text
from .models import Comment

admin.site.register(Text)
admin.site.register(Comment)
