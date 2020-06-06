from django import forms

from .models import FormDaftar

class form_daftar (forms.ModelForm):
    class Meta:
        model = FormDaftar
        fields = [
            'nama',
            'email',
            'tanggal_lahir',
            'gender',
            'alamat',
            'agree',
        ]
        widgets = {
            'nama':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Masukkan nama lengkap anda',
                },
            ),
            'email':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Masukkan email anda',
                },
            ),
            'tanggal_lahir':forms.SelectDateWidget(
                attrs = {
                    'class':'form-control',
                },
            ),
            'gender':forms.RadioSelect(
                attrs = {
                    'class':'form-check-input',
                },
                choices=(
                    ('P','Pria'),
                    ('W','Wanita'),
                )
            ),
            'alamat':forms.Textarea(
                attrs = {
                    'class':'form-control',
                },
            ),
            'agree':forms.CheckboxInput(
                attrs = {
                    'class':'form-check-input',
                },
            ),
        }

#ini cara lama
    '''
    nama = forms.CharField(
        max_length = 30,
        widget = forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Masukkan nama lengkap anda'
            },
        ),
    )

    email = forms.EmailField(
        widget = forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Masukkan email anda'
            },
        ),
    )

    tanggal_lahir = forms.DateField(
        widget = forms.SelectDateWidget(
            years=range(1945,2020,1),
            attrs = {
                'class':'form-control col-sm-2',
            },
        )
    )

    gender = forms.ChoiceField(
        widget = forms.RadioSelect(
            attrs={
                'class':'form-check-input',
            }
        ),
        choices=[
            ('P','Pria'),
            ('W','Wanita'),
        ]
    )

    alamat = forms.CharField(
        widget = forms.Textarea(
            attrs = {
                'class':'form-control',
                'placeholder':'Masukkan alamat lengkap anda'
            },
        ),
    )

    agree = forms.BooleanField(
        widget= forms.CheckboxInput(
            attrs={
                'class':'form-check-input',
            }
        )
    )'''