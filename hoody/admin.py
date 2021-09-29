from django.contrib import admin

from .models import *


class PostAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin),
admin.site.register(Category, CategoryAdmin),
admin.site.register(User),
admin.site.register(Neighborhood),
admin.site.register(Business),
admin.site.register(Comment),
