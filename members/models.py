from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    address1 = models.CharField(max_length=255, blank=True)
    address2 = models.CharField(max_length=255, blank=True)
    address3 = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name or "Unknown Contact"

class Member(models.Model):
    GENDER = [("Male", "Male"), ("Female", "Female")]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20, choices=GENDER, default="Male")
    phone = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    address1 = models.CharField(max_length=255, blank=True)
    address2 = models.CharField(max_length=255, blank=True)
    address3 = models.CharField(max_length=255, blank=True)

    class Meta:
        abstract = True  # Prevents Django from creating a separate table for Member

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Scout(Member):
    SECTION_CHOICES = [
        ('Beavers', 'Beavers'),
        ('Cubs', 'Cubs'),
        ('Scouts', 'Scouts'),
        ('Venturers', 'Venturers'),
    ]
    section = models.CharField(max_length=20, choices=SECTION_CHOICES)
    parent1 = models.ForeignKey(
        Contact, on_delete=models.SET_NULL, null=True, blank=True, related_name='scouts_parent1'
    )
    parent2 = models.ForeignKey(
        Contact, on_delete=models.SET_NULL, null=True, blank=True, related_name='scouts_parent2'
    )
    emergency = models.ForeignKey(
        Contact, on_delete=models.SET_NULL, null=True, blank=True, related_name='emergency'
    )
    special_requirements = models.TextField(blank=True)

class Scouter(Member):
    last_vetting_date = models.DateField()
    last_safeguarding_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"