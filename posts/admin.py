from django.contrib import admin
from posts.models import People,BlogContent,Comments
# Register your models here.

admin.site.register(People)
admin.site.register(BlogContent)
admin.site.register(Comments)
