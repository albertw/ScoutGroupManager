from django import forms
from members.models import Scout
from .models import AdventureSkillArea, AdventureSkillStage, Competency, ScoutSkillProgress

class SkillSelectionForm(forms.Form):
    """ Form to select section, skill area, and stage. """
    SECTION_CHOICES = Scout.SECTION_CHOICES  # Assuming SECTION is defined in Scout model

    section = forms.ChoiceField(choices=SECTION_CHOICES, required=True)
    skill_area = forms.ModelChoiceField(queryset=AdventureSkillArea.objects.all(), required=True)
    skill_stage = forms.ModelChoiceField(queryset=AdventureSkillStage.objects.all(), required=True)

"""
Need som funky ajax or similar to filter the skills by area
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "skill_area" in self.data:
            try:
                skill_area_id = int(self.data.get("skill_area"))
                self.fields["skill_stage"].queryset = AdventureSkillStage.objects.filter(skill_area_id=skill_area_id)
            except (ValueError, TypeError):
                pass
        else:
            self.fields["skill_stage"].queryset = AdventureSkillStage.objects.none()
"""
class ScoutCompetencyForm(forms.ModelForm):
    """ Form to update a scout's competency progress. """
    competencies_completed = forms.ModelMultipleChoiceField(
        queryset=Competency.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = ScoutSkillProgress
        fields = ["competencies_completed"]

    def __init__(self, *args, **kwargs):
        skill_stage = kwargs.pop("skill_stage", None)
        super().__init__(*args, **kwargs)
        if skill_stage:
            self.fields["competencies_completed"].queryset = skill_stage.competencies.all()


