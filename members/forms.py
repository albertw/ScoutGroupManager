from django import forms
from .models import Scouter


class ScouterForm(forms.ModelForm):
    class Meta:
        model = Scouter
        fields = "__all__"  # Includes all fields from the model

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Dates not required as we can populate from training import
        self.fields["last_vetting_date"].required = False
        self.fields["last_safeguarding_date"].required = False

        # Optional: Add custom help text
        self.fields["last_vetting_date"].help_text = "Enter the last vetting date."
        self.fields["last_safeguarding_date"].help_text = "Enter the last safeguarding training date."

