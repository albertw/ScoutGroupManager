from django.urls import path
from .views import skill_progress_view, home, get_skill_stages

urlpatterns = [
    path("skill-progress/", skill_progress_view, name="skill_progress"),
    path('get_skill_stages/<int:skill_area_id>/', get_skill_stages, name='get_skill_stages'),
    path('', home, name='home'),  # Home view for the root URL of this app
]