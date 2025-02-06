from django import forms

class CreateNewList(forms.Form):
    # set the fields for your forms // exact as database
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(required=False)
