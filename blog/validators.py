from django.core.exceptions import ValidationError

def clean_judul(value):
        judul_input = value

        if judul_input == 'bukan judul':
            raise forms.ValidationError('judul tidak di perbolehkan')
    
