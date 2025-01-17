from django.db import models
from members.models import Scout  # Assuming Scout model is in members app

class AdventureSkillArea(models.Model):
    """ Represents the 9 skill areas (e.g., Hillwalking, Camping). """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class AdventureSkillStage(models.Model):
    """ Represents a specific stage (1-9) within a skill area. """
    skill_area = models.ForeignKey(AdventureSkillArea, on_delete=models.CASCADE, related_name="stages")
    stage_number = models.PositiveIntegerField()  # 1-9

    class Meta:
        unique_together = ("skill_area", "stage_number")  # Ensures unique stage per skill area

    def __str__(self):
        return f"{self.skill_area.name} - Stage {self.stage_number}"

class Competency(models.Model):
    """ Represents individual competencies a scout must achieve to complete a stage. """
    skill_stage = models.ForeignKey(AdventureSkillStage, on_delete=models.CASCADE, related_name="competencies")
    competency = models.TextField(null=True, blank=True)  # "I can pitch a tent", "I have been on a camp", etc.
    description = models.TextField()

    def __str__(self):
        return f"{self.skill_stage.skill_area.name} - Stage {self.skill_stage.stage_number}: {self.competency}"

class ScoutSkillProgress(models.Model):
    """ Tracks a scout’s progress in an Adventure Skill area and stage. """
    scout = models.ForeignKey(Scout, on_delete=models.CASCADE, related_name="skill_progress")
    skill_stage = models.ForeignKey(AdventureSkillStage, on_delete=models.CASCADE, related_name="scout_progress")
    competencies_completed = models.ManyToManyField(Competency, blank=True)  # Tracks completed competencies
    # TODO: It's possible to do any competency with any skill and stage this way :)
    badge_awarded = models.BooleanField(default=False)

    class Meta:
        unique_together = ("scout", "skill_stage")  # Ensures one progress entry per scout per stage

    def check_completion(self):
        """ Check if the scout has completed all required competencies for this stage. """
        required_competencies = self.skill_stage.competencies.count()
        completed_competencies = self.competencies_completed.count()
        return completed_competencies >= required_competencies

    def award_badge(self):
        """ Awards badge if all competencies are completed. """
        if self.check_completion():
            self.badge_awarded = True
            self.save()

    def __str__(self):
        return f"{self.scout} - {self.skill_stage} - {'Awarded' if self.badge_awarded else 'In Progress'}"
