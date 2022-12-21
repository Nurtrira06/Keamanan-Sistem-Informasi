from django import forms

# class nameclass(forms.Form):
#     namac = forms.CharField()
#     alamatc = forms.CharField()

class classform(forms.Form):
    namac = forms.CharField(
        label = 'Nama Lengkap',
        widget = forms.TextInput(
            attrs={
                'class':'field padding-bottom--24',
                'type':'nama',
                'placeholder':'Masukkan Nama',
            }
        )
    )