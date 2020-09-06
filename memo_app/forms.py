from django import forms
from .models import Memo

CHOICE_FIELD_RECODE_NUMBERS = (
    ('10', '10件'),
    ('15', '15件'),
    ('30', '30件'),
)

CHOICE_FIELD_ORDER_OPTION = (
    ('new', '新着順'),
    ('old', '古い順'),
)

class RecordNumberForm(forms.Form):
    record_number = forms.ChoiceField(
        widget=forms.Select(attrs={'onchange': 'submit(this.form)'}), 
        choices=CHOICE_FIELD_RECODE_NUMBERS
    )

class SetOrderOption(forms.Form):
    order_option = forms.ChoiceField(
        widget=forms.Select(attrs={'onchange': 'submit(this.form'}),
        choices=CHOICE_FIELD_ORDER_OPTION
    )

class PostForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ['content']
        widgets = {
            'content': forms.Textarea
        }