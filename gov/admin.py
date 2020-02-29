from django.contrib import admin

#Register your models here.
from .models import Post
from .models import Category
from .models import event
from .models import Gallery
from .models import contact
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('category', )
    prepopulated_fields = {'slug': ('category',)}




class PostAdmin(admin.ModelAdmin):
    search_fields = ('coursename', )
    prepopulated_fields = {'slug': ('coursecategory',)}
    fields = ('coursename', 'amount')




admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.register(event)
admin.site.register(Gallery)
admin.site.register(contact)

