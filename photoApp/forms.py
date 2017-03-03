from django import forms


class documentForm(forms.Form):
    #picture = forms.FileField()
    picture = forms.CharField()
    name = forms.CharField()
    room_code = forms.CharField()


