from dal import autocomplete

from django import forms
from .models import Project, Category, Client


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project

        fields = ('__all__')

        widgets = {
            'client': autocomplete.ModelSelect2(
              url='projects:client-autocomplete'
            )
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('__all__')


# class ClientForm(forms.ModelForm):
#     class Meta:
#         model = Client
#         fields = ('__all__')
        