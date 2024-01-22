from django import forms

from Personapp.models import Person_profile, Course


MATERIAL_CHOICES = [
   ('Note Book','Note Book'),
   ('Pen','Pen'),
   ('Exam Paper','Exam Paper')
]

class Personform(forms.ModelForm):
    material = forms.MultipleChoiceField(label='Required Materials', choices=MATERIAL_CHOICES, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Person_profile
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateTimeInput(attrs={'class':'form-control ','id':'datepicker'}),
            'age':forms.TextInput(attrs={'class': 'form-control'}),
            'gender':forms.Select(attrs={'class': 'form-control'}),
            'phone_number':forms.TextInput(attrs={'class': 'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'class': 'form-control'}),
            'department':forms.Select(attrs={'class': 'form-control'}),
            'course':forms.Select(attrs={'class':'form-control'}),
            'purpose':forms.Select(attrs={'class':'form-control'}),
            'Material':forms.CheckboxSelectMultiple()

            

            }

        def __init__(self, *args, **kwargs):
           super().__init__(*args, **kwargs)
           self.fields['course'].queryset = Course.objects.none()



     