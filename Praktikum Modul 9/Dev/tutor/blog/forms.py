from django import forms
from blog.models import Post

# class nameclass(forms.Form):
#     namac = forms.CharField()
#     alamatc = forms.CharField()

# class classform(forms.Form):
#     namac = forms.CharField(
#         label = 'Nama Lengkap',
#         widget = forms.TextInput(
#             attrs={
#                 'class':'field padding-bottom--24',
#                 'type':'nama',
#                 'placeholder':'Masukkan Nama',
#             }
#         )
#     )

class classform(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'body',
            'email'
        ]

        widgets={
            'title': forms.TextInput(
                attrs = {
                    'class' : 'form',
                    'placeholder' : 'Masukan Judul',
            }
            )
        }

