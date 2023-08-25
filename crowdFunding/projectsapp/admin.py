from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(ProjectRating)
admin.site.register(ProjectReport)
admin.site.register(Projects_pictures)
admin.site.register(Tags)
admin.site.register(Comment)
admin.site.register(CommentReport)
admin.site.register(Replay)
admin.site.register(ReplayReport)

