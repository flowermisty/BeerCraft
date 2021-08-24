from django.contrib import admin
from .models import DetailInfo, Comment

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(DetailInfo)
admin.site.register(Comment)
# Register your models here.
