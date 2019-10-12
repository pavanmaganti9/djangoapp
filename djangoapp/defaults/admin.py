from django.contrib import admin

# Register your models here.
from .models import blog,contact

class BlogAdmin(admin.ModelAdmin):
	search_fields = ['title','tag']
	list_display = ['title','email','tag','author','date']
	list_editable = ['tag']
	list_filter = ['tag']
	#readonly_fields = ['tag']
	#prepopulated_fields = {"slug": ['tag']}
# Register your models here.
admin.site.register(blog, BlogAdmin)

admin.site.register(contact)