from django import forms

from .models import ItYear
from bootstrap_datepicker_plus.widgets import DateTimePickerInput


class ItForm(forms.ModelForm):
    class Meta:
        model = ItYear
        fields = ('department', 'initiator',
                  'phone_number', 'description',)
        widgets = {
            'department': forms.Select(attrs={'class': 'form-control'}),
            'initiator': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ф.И.О'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'type': 'tel', 'data-tel-input': True,
                                                   'placeholder': 'Пример ввода 89278679792', 'maxlength': '18'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Краткое описание заявки'}),
        }


class EditItForm(forms.ModelForm):

    class Meta:
        model = ItYear
        fields = ('comment', 'performer', 'completed', 'date_completed',)
        widgets = {
            'performer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ф.И.О'}),
            'date_completed': DateTimePickerInput(),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Комментарий к заявке'}),
        }
