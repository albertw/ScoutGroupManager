import os
import django
import sys
import json

sys.path.append("../../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ScoutGroupManager.settings")

django.setup()

from badges.models import AdventureSkillStage, AdventureSkillArea, Competency
from members.models import Scout

from django.contrib.auth import get_user_model


def create_admin():
    User = get_user_model()
    User.objects.create_superuser('admin', 'admin@example.com', 'password')


def populate_adventure_skills():
    with open("adventureskills.json", 'r') as file:
        data = json.load(file)

    for skill_area_name, stages_data in data.items():
        skill_area, res = AdventureSkillArea.objects.update_or_create(name=skill_area_name)
        for stage_name, competencies_list in stages_data.items():
            stage_number = int(stage_name.split()[1])
            stage, res = AdventureSkillStage.objects.update_or_create(skill_area=skill_area, stage_number=stage_number)
            for competency_description in competencies_list:
                Competency.objects.update_or_create(skill_stage=stage, competency=competency_description)


def populate_members():
    with open("samplescouts.json", 'r', encoding="utf-8") as file:
        data = json.load(file)

    for scout in data:
        Scout.objects.get_or_create(first_name=scout['first_name'], last_name=scout['last_name'],
                                    gender=scout['gender'], section=scout['section'],
                                    date_of_birth=scout['date_of_birth'])


populate_adventure_skills()
populate_members()
create_admin()
