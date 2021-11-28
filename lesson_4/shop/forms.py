from django import forms

from .models import Goods


class GoodCreateForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GoodCreateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fielads.items():
            field.widget.attrs['class'] = 'form-control'
