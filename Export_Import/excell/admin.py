from django.contrib import admin

from . models import home
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(home, ImportExportModelAdmin)


