from django import forms

from .models import Company,Job,Candidate

class companyform(forms.ModelForm):
    class Meta:
        model=Company
        fields ='__all__'


    # def clean(self):
    #     super(companyform,self).clean()
    #     co_regno = self.cleaned_data.get('co_regno')
    #
    #     if co_regno <1:
    #         self._errors['co_regno']=self.error_class(['Reg Number is not valid'])
    #
    #     return self.cleaned_data

class jobform(forms.ModelForm):
    class Meta:
         model=Job
         fields ='__all__'

class candidateform(forms.ModelForm):
    class Meta:
         model=Candidate
         fields ='__all__'


