from django.contrib import admin
from .models import Scout, Scouter, Contact
from .forms import ScouterForm  # Import the custom form

@admin.register(Scout)
class ScoutAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'section', 'date_of_birth')
    search_fields = ('first_name', 'last_name')
    list_filter = ('section',)

class ScouterAdmin(admin.ModelAdmin):
    form = ScouterForm  # Use the custom form
    list_display = ("first_name", "last_name", "last_vetting_date", "last_safeguarding_date")
    search_fields = ("first_name", "last_name")
    fieldsets = (
        ("Personal Info", {
            "fields": ("first_name", "last_name", "date_of_birth", "phone", "email"),
        }),
        ("Address", {
            "fields": ("address1", "address2", "address3"),
        }),
        ("Vetting & Safeguarding", {
            "fields": ("last_vetting_date", "last_safeguarding_date"),
        }),
    )
admin.site.register(Scouter, ScouterAdmin)  # Use custom admin
admin.site.register(Contact)  # Use custom admin