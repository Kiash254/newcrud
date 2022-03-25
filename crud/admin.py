from django.contrib import admin
from .models import Detail
# Register your models here.

admin.site.site_header="ADMIN PANEL"
admin.site.site_title="ADMIN PANEL"


admin.site.register(Detail)
