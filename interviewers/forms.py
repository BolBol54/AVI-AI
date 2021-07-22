from django import forms
from .models import Companies, Job, Questions, Interviews, Interviewees
from django.contrib.postgres.forms import SimpleArrayField
from . import models

from django.forms import ModelChoiceField, formset_factory


class InterviewForm(forms.ModelForm):
    # jobs = Job.objects.values('name')
    Job = forms.ModelChoiceField(queryset=Job.objects.all(), empty_label="Choose A Job",required=True)
    title = forms.CharField(widget=forms.TextInput,max_length=200,required=True)
    description = forms.CharField(widget=forms.TextInput,max_length=300,required=True)
    # Questions = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
    #                           choices=Questions.objects.values('answer'))

    # Time_Limit = forms.CharField(widget=forms.TextInput(
    #     attrs={"placeholder": "Write A Subject"}))
    class Meta:
        model = Interviews
        fields = ["Job",'title','description']

class JobForm(forms.ModelForm):
    name = forms.CharField(required=True,label="Job Title",max_length=100)
    description = forms.CharField(required=True,label="Job Description",max_length=100, widget= forms.TextInput
                           (attrs={'placeholder':'Enter Here The Job Decsription '}))

    class Meta:
        model = Job
        fields = ['name',"description"]

class QuestionForm(forms.ModelForm):
        # question / answer / questionDur
        OPTIONS = (
            ("30", "30 sec"),
            ("1", "1 min"),
            ("2", "2 mins"),
            ("5", "5 mins"),
            ("10", "10 mins"),
            ("15", "15 mins"),
        )
        question = forms.CharField(required=True, label="Question", max_length=100,
                                   widget= forms.TextInput(attrs={'placeholder': 'Write The Question '}))
        answer = forms.CharField(required=False,label="Answer", max_length=100, widget=forms.TextInput
        (attrs={'placeholder': 'Write The Answer (if exist) '}))

        questDur = forms.ChoiceField(required=True, choices=OPTIONS,label="Question Duration")
        # skills = SimpleArrayField(forms.CharField(max_length=100,))
        skills = forms.CharField(required=True,label="Skill(s)",
                                 widget=forms.TextInput(attrs={"placeholder":"Comm/Tech"}))
        description = forms.CharField(required=True,label="Notes")

        class Meta:
            model = Questions
            fields = ['question', "answer","questDur","skills","description"]

class Interviewee(forms.ModelForm):
    name = forms.CharField(required=True,label="Name",max_length=100)
    email = forms.EmailField(required=True)


    class Meta:
        model = Interviewees
        fields=['name','email']
        exclude = ('state',)

