from django.contrib import admin
from .models import Dictionary

# Register your models here.

class DictionaryAdmin(admin.ModelAdmin):
	class meta:
		model=Dictionary

admin.site.register(Dictionary,DictionaryAdmin)