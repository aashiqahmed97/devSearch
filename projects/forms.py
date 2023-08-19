from django.forms import ModelForm, widgets
from django import forms
from .models import project , Review

class projectForm(ModelForm):
    class Meta:
        model= project
        fields=['title','featured_image' ,'description','demo_link','source_link','tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
    def __init__(self,*args,**kwargs):
        super(projectForm, self).__init__(*args,**kwargs) 
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']
        labels = {
            'value': 'Place your vote',
            'body': 'Add a comment with your vote'
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'}) 
