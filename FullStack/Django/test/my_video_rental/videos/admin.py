from django.contrib import admin
from . import models

class MovieAdmin(admin.ModelAdmin):
    fields = ['release_year','title','length']
    search_fields = ['title']
    list_filter = ['release_year','length']
    list_display = ['title','release_year','length']
    list_editable = ['length']
class CustomerAdmin(admin.ModelAdmin):
    fields = ['first_name','last_name','phone']

admin.site.register(models.Customer,CustomerAdmin)
admin.site.register(models.Movie,MovieAdmin)



