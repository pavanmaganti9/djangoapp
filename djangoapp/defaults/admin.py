from django.contrib import admin

# Register your models here.
from .models import blog,contact

class BlogAdmin(admin.ModelAdmin):
	search_fields = ['title','tag']
	list_display = ['title','email','tag','author','date']
	list_editable = ['tag']
	list_filter = ['tag']
	save_as = True
	save_on_top = True # save buttons on top too
	#readonly_fields = ['tag']
	#prepopulated_fields = {"slug": ['tag']}
	
	#fields = ('featured',('title','email'))
	fieldsets = (
		(None, {
			'fields' : (
				('title','email','tag','featured','color'),
			)
		}),
		('Author, Dates', {
			#'classes' : ('collapse',),
			'classes' : ('wide',),
			#'fields':('author','date')
			'fields':(('author','date')) #side by side
		})
	)
	
	radio_fields = {'featured':admin.HORIZONTAL}
	
# Register your models here.
admin.site.register(blog, BlogAdmin)

admin.site.register(contact)