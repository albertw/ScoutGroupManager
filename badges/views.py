from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelformset_factory
from members.models import Scout
from .models import AdventureSkillStage, AdventureSkillArea, Competency, ScoutSkillProgress
from .forms import SkillSelectionForm, ScoutCompetencyForm

from django.http import JsonResponse
from .models import AdventureSkillStage


def skill_progress_view(request):
    form = SkillSelectionForm(request.GET or None)  # Prepopulate from GET request
    scouts = []
    skill_stage = None
    competency_forms = []
    progress_forms = []

    if "section" in request.GET and "skill_area" in request.GET and "skill_stage" in request.GET:
        section = request.GET.get("section")
        skill_stage = get_object_or_404(AdventureSkillStage, id=request.GET.get("skill_stage"))
        scouts = Scout.objects.filter(section=section)

        # Create or get progress records for each scout
        progress_forms = []
        for scout in scouts:
            progress, created = ScoutSkillProgress.objects.get_or_create(scout=scout, skill_stage=skill_stage)
            form = ScoutCompetencyForm(instance=progress, skill_stage=skill_stage)
            progress_forms.append((scout, form))

    if request.method == "POST":
        skill_stage = get_object_or_404(AdventureSkillStage, id=request.POST.get("skill_stage"))
        scouts = Scout.objects.filter(section=request.POST.get("section"))

        print(scouts)
        print(skill_stage)
        for scout in scouts:
            progress = ScoutSkillProgress.objects.filter(scout=scout, skill_stage=skill_stage)
            form = ScoutCompetencyForm(request.POST, instance=progress, skill_stage=skill_stage)
            if form.is_valid():
                form.save()

        return redirect(f"{request.path}?section={request.POST.get('section')}&skill_area={skill_stage.skill_area.id}&skill_stage={skill_stage.id}")

    return render(request, "badges/skill_progress.html", {
        "form": form,
        "scouts": scouts,
        "skill_stage": skill_stage,
        "progress_forms": progress_forms,
    })



def get_skill_stages(request, skill_area_id):
    # Fetch skill stages filtered by the selected skill_area
    skill_stages = AdventureSkillStage.objects.filter(skill_area_id=skill_area_id)

    # Prepare the data to send back as JSON
    data = {
        'skill_stages': [{'id': stage.id, 'name': AdventureSkillArea.objects.get(id=skill_area_id).name,
                          'number': stage.stage_number} for stage in skill_stages]
    }

    return JsonResponse(data)


def home(request):
    return render(request, 'badges/home.html')