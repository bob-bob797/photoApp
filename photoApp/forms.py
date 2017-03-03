from django import forms


class documentForm(forms.Form):
    picture = forms.FileField()
    name = forms.CharField()
    room_code = forms.CharField()


