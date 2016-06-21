from django import forms

class newsForm(forms.Form):
    heading = forms.CharField(max_length=150)
    fileform = forms.FileField()
    description = forms.CharField(widget=forms.Textarea)