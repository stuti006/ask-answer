from django.contrib import admin
from .models import *

class QuestionAdmin(admin.ModelAdmin):
    list_display=('title','user')
    search_fields=('title','detail')
admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer)

# class CommentAdmin(admin.ModelAdmin):
#     list_display=('answer','comment')
admin.site.register(Comment)

# class UpvoteAdmin(admin.ModelAdmin):
#     list_display=('answer','user')
admin.site.register(UpVote)

# class DownvoteAdmin(admin.ModelAdmin):
#     list_display=('answer','user')
admin.site.register(DownVote)

# admin.site.register(CustomUser)
