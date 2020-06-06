from django import forms
from .models import Post

class CreatePost (forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'judul',
            'body',
            'category',
        ]
        widgets = {
            'judul' : forms.TextInput(
                attrs={
                    'class':'form-control col-4',
                },
            ),
            'body' : forms.Textarea(
                attrs={
                    'class':'form-control col-4',
                },
            ),
            'category' : forms.Select(
                attrs={
                    'class':'form-control col-4',
                },
            ),
        }
    def clean_judul(self):
        judul_input = self.cleaned_data.get('judul')

        if judul_input == 'bukan judul':
            raise forms.ValidationError('judul tidak di perbolehkan')
        
        return judul_input
