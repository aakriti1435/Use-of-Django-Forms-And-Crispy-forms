from django import forms
from .models import Snippet

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label="E-mail")
    category = forms.ChoiceField(choices=[('question','Question'),('other','Other')])
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #self.helper = FormHelper 
        #self.helper.form_method = 'post '

class SnippetForm(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ('name','body')

 # pip install django-crispy-forms