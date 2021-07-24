from datetime import timedelta, date

from django.contrib.auth.models import User
from django.db import models
from django.utils.datetime_safe import datetime
# Create your models here.

class Job(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    created_by = models.ForeignKey(User,related_name='createdBy',default="", on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name


class Questions(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100, default=None)
    questDur = models.CharField(max_length=100, default=None)
    skills = models.CharField(max_length=200,default=" ")
    description = models.CharField(max_length=300,default="")
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.question


class Interviews(models.Model):
    title = models.CharField(max_length=300,default="")
    job = models.ForeignKey(Job,related_name='interviews',on_delete=models.CASCADE)
    description = models.CharField(max_length=300,default="")
    created_by = models.ForeignKey(User,related_name='User',default="",on_delete=models.CASCADE)
    Expiration_date= models.DateTimeField(default=date.today()+timedelta(3))
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

class InterviewQuestions(models.Model):
    order = models.IntegerField(default=0)
    interview = models.ForeignKey(Interviews, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    class Meta:
        ordering = ['order']

    def __str__(self):
        # template = '{0.order} {0.question.id} {0.question.answer} {0.question.questDur} {0.interview}'
        # return template.format(self)
        return self.question.id


class Companies(models.Model):
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    phoneNo = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Interviewees(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, default="")
    send_by = models.ForeignKey(User,related_name="interviewee_send_by",on_delete=models.CASCADE)
    state = models.CharField(max_length=100, default="Waiting")
    def __str__(self):
        return self.name
class Applicants(models.Model):
    interview = models.ForeignKey(Interviews, related_name='applicant', on_delete=models.CASCADE)
    interviewee = models.ForeignKey(Interviewees, related_name='applicant', on_delete=models.CASCADE)
    invitationLink = models.CharField(max_length=300,default="")

    def __str__(self):
        return self.state

    def get_state(self):
        ret = ''
        print(self.applicants.all())
        # use models.ManyToMany field's all() method to return all the Department objects that this employee belongs to.
        for app in self.applicant.all():
            ret = ret + app.state + ','
        # remove the last ',' and return the value.
        return ret[:-1]

class Report(models.Model):
    applicant= models.ForeignKey(Applicants,related_name="report",on_delete=models.CASCADE)
    report = models.FileField(upload_to='videos/', null=True, verbose_name="")

class CompanyUsers(models.Model):
    company = models.ForeignKey(Companies,related_name='companyUsers', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='companyUsers', on_delete=models.CASCADE)

class ApplicantQues(models.Model):
    applicant= models.ForeignKey(Applicants,related_name="appQues",on_delete=models.CASCADE)
    question = models.ForeignKey(Questions,related_name="appQues",on_delete=models.CASCADE)
    videoAns = models.FileField(upload_to='videos/', null=True, verbose_name="")

    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'
