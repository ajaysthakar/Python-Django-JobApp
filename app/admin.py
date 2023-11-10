from django.contrib import admin

from app.models import Author, JobPost, Location, Skills

class JobAdmin(admin.ModelAdmin):
    list_display =('title','description','salary','date',)
    list_filter = ('date','salary')
    search_fields = ['title','description']
    search_help_text = "Write in your query and hit enter"
    #fields =(('title','description'),'salary')
    #exclude = ('salary','')
    fieldsets = (
        ('Basic Info',{
            'fields':('title','description','type')
        }),
        ('More Info',{
            #'classes':('collapse',),
            'fields':(('salary','expiry'),'slug','location','author','skill')
        }),
    )

class Skillset(admin.ModelAdmin):
    list_display=['name']

# Register your models here.
admin.site.register(JobPost,JobAdmin)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skills,Skillset)