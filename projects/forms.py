from django import forms
from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ("title", "description", "featured_img", "source_link", "demo_link", "tags")
        widgets = {
            "tags": forms.CheckboxSelectMultiple()
        }



    def __init__(self, *args, **kwargs) -> None:
        super(ProjectForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                "class":"input input--text",
            })