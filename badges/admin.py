from django.contrib import admin
from .models import AdventureSkillArea, AdventureSkillStage, Competency, ScoutSkillProgress

admin.site.register(AdventureSkillArea)
admin.site.register(AdventureSkillStage)
admin.site.register(Competency)

@admin.register(ScoutSkillProgress)
class ScoutSkillProgressAdmin(admin.ModelAdmin):
    list_display = ("scout", "skill_stage", "badge_awarded")
    filter_horizontal = ("competencies_completed",)  # Enables a better UI for selecting competencies
