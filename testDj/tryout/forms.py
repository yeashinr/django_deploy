from django.forms import ModelForm
from django import forms
from .models import internalapp,portList
from django.contrib.admin.widgets import FilteredSelectMultiple

class appForm(ModelForm):
    
     port = forms.ModelMultipleChoiceField(internalapp.objects.all(),widget=
                FilteredSelectMultiple("Port",False,attrs={'rows':'10'}))
     class Meta:
        model = internalapp
        fields = '__all__'
        labels = {'appGrpNm': ('Application Group')}
        help_texts = {'appGrpNm': ('Enter a date between now and 4 weeks (default 3).')}
        #error_messages = {'appGrpNm':'Please fill out this field'}
     class Media:
        css = {'all': ('/static/admin/css/widgets.css',),     
                }
        js = ('/admin/jsi18n/',)



    # ports = forms.ModelMultipleChoiceField(
    #             queryset=portList.objects.all(),
    #             widget=FilteredSelectMultiple(
    #                 'Personnel', is_stacked=False),
    #             label='')
    # class Meta:
    #     model = internalapp
    #     fields = '__all__'
    #     widgets = { 
    #         'ports': FilteredSelectMultiple(queryset=portList.objects.all())
    #     }
    # class Media:
    #     css = {'all': ('/static/admin/css/widgets.css',), }
    #     js = ('/admin/jsi18n/',)

    # def __init__(self, parents=None, *args, **kwargs):
    #     r= super(appForm, self).__init__(*args, **kwargs)
    #     self.fields['ports'] = forms.ModelMultipleChoiceField(
    #             queryset=portList.objects.all(),
    #             widget=FilteredSelectMultiple(
    #                 'hell', is_stacked=False),
    #             label='')
    #     return r
class tryoutform(forms.Form):
    name = forms.CharField(required=False,initial='Please provide your name')
    email = forms.EmailField(label='Your email')
    comment = forms.CharField(widget=forms.Textarea)
    error_css_class = 'error'
    required_css_class = 'bold' 