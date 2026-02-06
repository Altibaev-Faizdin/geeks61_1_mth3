from django import forms
from prog_lang.models import ProgLang


class ProgLangForm(forms.ModelForm):
    class Meta:
        model = ProgLang
        fields = "__all__"



