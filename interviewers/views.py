from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .forms import JobForm, InterviewForm , QuestionForm , Interviewee
from interviewers.models import Interviews, Job, Questions, Interviewees, Applicants, ApplicantQues
import time
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, send_mass_mail, EmailMultiAlternatives
from django.http import HttpResponse, StreamingHttpResponse, HttpResponseServerError, JsonResponse
from django.conf import settings
from django.views.decorators import gzip
import cv2
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.templatetags.static import static


def report(request,interviewee_id):
    Int = Interviewees.objects.get(pk=interviewee_id)
    str = Int.name.lower()
    name = str.replace(" ", "")
    html = "report/%s.html" %name
    video = "/video/%s.mp4" %name
    return  render(request,html,{"Interviewee":Int,"video":video})
def record(request):
    return  render(request,"video.html")
# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required(login_url='/login/?next=')
def dashboard(request):
    user = request.user
    interviews = Interviews.objects.count()
    jobs = Job.objects.count()
    return render(request, 'dashboard.html',{"user":user,'interviews':interviews,'jobs':jobs})

@login_required(login_url='/login/?next=')
def addJob(request):
        job = JobForm()
        if request.method == "POST":
            job = JobForm(request.POST)
            if job.is_valid():
                new = Job.objects.create(
                            name=request.POST['name'],
                            description=request.POST['description'],
                                created_by=request.user
                        )
                return redirect("jobs")
        return render(request,"job/addJob.html", {"job":job})

def Jobs(request):
    jobs = Job.objects.all()
    count = Job.objects
    return render(request, "job/jobs.html", {"jobs": jobs,'count':count})

@login_required(login_url='/login/?next=')
def jobDelete(request,job_id):
    job = Job.objects.get(id = job_id)
    job.delete()
    return redirect("jobs")

    # def post_reply(request, board_id, topic_id):
    #     topic = get_object_or_404(Topics, board__pk=board_id, pk=topic_id)

@login_required(login_url='/login/?next=')
def eachJob(request,job_id):
    job = Job.objects.get(id = job_id)
    return render(request,"job/job.html" , {"job":job})

    # def post_reply(request, board_id, topic_id):
    #     topic = get_object_or_404(Topics, board__pk=board_id, pk=topic_id)


@login_required(login_url='/login/?next=')
def addInterview(request):
    interviewForm = InterviewForm()
    questForm = QuestionForm()
    # questForm = formset_factory(QuestionForm,extra=2)

    if request.method == "POST":
        print(request.POST)
        interview = InterviewForm(request.POST)

        if interview.is_valid():
            job = Job.objects.get(pk=request.POST['Job'])
            title = request.POST['title']
            user = request.user
            description =request.POST["description"]
            inview = Interviews.objects.create(title=title, job=job, description=description,created_by=user)
            # return redirect('interview', interview_id=inview.pk, kwargs={'interview': inview,'question':questForm})
            return redirect("addInterQues", interview_id=inview.pk)
        else:
            return render(request, "interview/addInterview.html", {"interview": interview})
    return render(request,'interview/addInterview.html', {'interview': interviewForm,'question':questForm})

    #     #     print("in")
    # publications = models.ManyToManyField(Publication)
# def duration(td):
#     total_seconds = int(td.total_seconds())
#     hours = total_seconds // 3600
#     minutes = (total_seconds % 3600) // 60
#     return '{} hours {} min'.format(hours, minutes)
# import time
# >>> time.strftime('%H:%M:%S', time.gmtime(12345))
# '03:25:45'


@login_required(login_url='/login/?next=')
def addQuestions(request,interview_id):
    interview = Interviews.objects.get(pk=interview_id)
    questForm = QuestionForm()
    questions = arr(interview.interviewquestions_set.values_list('question_id'),Questions)
    if request.method == "POST":
        question = QuestionForm(request.POST)
        if question.is_valid():
            if request.POST['answer'] == "" : answer = " "
            else: answer =request.POST['answer']

            order = interview.interviewquestions_set.count()
            if(request.POST["questDur"] == "30"):
                dur = "30 sec"
            else: dur= request.POST['questDur'] + "mins"

            quest = Questions.objects.create(
                question = request.POST['question'],
                answer= answer,
                questDur=dur,
                skills= request.POST['skills'],
                description= request.POST["description"]
            )
            interview.interviewquestions_set.create(
                order= order +1,
                question_id = quest.id
            )
            return redirect("interview", interview_id=interview.pk)
        else:
            print("not done")
            questForm = QuestionForm(question.errors)
            return render(request, "interview/addinterviewQues.html", {"interview": interview, "questForm": questForm,
                                                                'questions': questions})
    return render(request, "interview/addinterviewQues.html", {"interview": interview, "questForm": questForm,
                                                        'questions': questions})
            # job = Job.objects.get(id = request.POST['job'])
            # Interviews.objects.create(
            #     title=request.POST['title'],
            #     job_id=request.POST['job'],
            #     created_by=request.user
            # )
            # interview.save()

    # job = get_object_or_404(Job, pk=job_id)

@login_required(login_url='/login/?next=')
def allInterviews(request):
    interviews = Interviews.objects.all()
    return render(request, "interview/interviews.html", {"interviews" : interviews})


@login_required(login_url='/login/?next=')
def interviewDelete(request,interview_id):
    interview = Interviews.objects.get(id = interview_id)
    interview.delete()
    return redirect("interviews")

@login_required(login_url='/login/?next=')
def questDelete(request,interview_id,question_id):
    interview = Interviews.objects.get(id=interview_id)
    question = interview.interviewquestions_set.get(question_id = question_id)
    question.delete()
    return redirect("interview",interview_id=interview.pk)


def my_mail(request):
    subject = "Greetings from AVI"
    html_content = render_to_string("mail.html",{"title":"Interview Invitation",})
    text = strip_tags(html_content)

    # html_message = 'Hey there' \
    #                '<p>Your Interview Invitation for the vacancy</p>' \
    #                '<a href="http://127.0.0.1:8000/login" class="btn btn-dark">Start Now</a>'
    to = request.POST["email"]
    res = EmailMultiAlternatives(subject, text, settings.EMAIL_HOST_USER, [to])
    res.attach_alternative(html_content,"text/html")
    res.send()
    if (res == 1):
        msg = "Mail Sent Successfully."
    else:
        msg = "Mail Sending Failed."
    return HttpResponse(msg)

def arr(var,model):

    list = []
    for v in var:
        val = model.objects.get(pk=v[-1])
        list.append(val)
    return list


@login_required(login_url='/login/?next=')
def interview(request,interview_id):
    interview = Interviews.objects.get(pk=interview_id)
    questions = arr(interview.interviewquestions_set.values_list('question_id'),Questions)
    interviewee = Interviewee()
    interviewees = arr(interview.applicant.values_list("interviewee_id"),Interviewees)
    state=[]
    list = []
    for q in questions:
        q.skills = q.skills.split("/")
        list.append(q.skills)
    if request.method == "POST":
        interviewee = Interviewee(request.POST)
        if interviewee.is_valid():
            name = request.POST['name']
            email =request.POST['email']
            send_by = request.user
            my_mail(request)
            app=Interviewees.objects.create(name=name, email=email,send_by=send_by,state="Waiting")
            invitationLink = "startinterview/"+ str(app.id)
            app.applicant.create(
                interview = interview,
                invitationLink=invitationLink
            )
            return redirect("interview",interview_id)


    return render(request, "interview/interview.html", {"interview": interview,'questions': questions,
                                                        "intervieweeForm":interviewee,"interviewees":interviewees,
                                                        "skills":list})

###############################################################################################################
def onlineInterview(request,applicant_id):
    Applicant = Applicants.objects.get(pk=applicant_id)
    interview = Interviews.objects.get(pk=Applicant.interview_id)
    questions = arr(interview.interviewquestions_set.values_list('question_id'),Questions)
    if request.method == "POST":
        if "start" in request.POST:
            array = interview.interviewquestions_set.values_list('question_id')
            return render(request, "applicant/questions.html",{"question":questions[0],'interview':interview,})
        if "next" in request.POST:
            print(request.POST)

            # name = link.split("/")[3]
            # ApplicantQues.objects.create(
            #     applicant= Applicant,
            #     question= questions[0],
            #     videoAns= request.POST['answerVideo']
            # )
                # na = str(questions[0].id) + str()
                # # cv2.VideoWriter("/static/video/filename.mp4", name, 20, (320, 180))
                #
                # # print(name)
                # file = open(os.path.join(django_settings.STATIC_ROOT, f'video_{link}.json'), 'w')
                # print(file)

            return render(request,"video.html")

            questions.pop(0)
            last = ""
            if len(questions) == 1:
                last = "last"
            return render(request, "applicant/questions.html",{"applicant": applicant_id,"question":questions[0],'interview':interview,
                                                             "last":last})
        if "end" in request.POST:
            print("end")
    try:
        return render(request, "applicant/startinterview.html", {"applicant": Applicant, "interview": interview,
                                                                 "questions": questions})
    except HttpResponseServerError:
        print("error")

@csrf_exempt
def upload(request):
    # if request.method == "POST":
    print(request.POST.get("file"))
    HttpResponse("HELLO")
    return  HttpResponse("HELLO")
    # src = request.POST.get('video-blob')
    #     filname =request.POST.get('video-filename')
    #
    #     ApplicantQues.objects.create(
    #     )

def deleteInterviewee(request,interviewee_id):

    int = Interviewees.objects.get(pk=interviewee_id)
    app = int.applicant.all()




    # to capture video class
def get_frame():
    camera = cv2.VideoCapture(0)
    while True:
        _, img = camera.read()
        imgencode = cv2.imencode('.jpg', img)[1]
        stringData = imgencode.tostring()
        yield (b'--frame\r\n'b'Content-Type: text/plain\r\n\r\n' + stringData + b'\r\n')
        del (camera)

@gzip.gzip_page
def dynamic_stream(request, stream_path="video"):
    try:
        return StreamingHttpResponse(get_frame(), content_type="multipart/x-mixed-replace;boundary=frame")
    except: return "error"

def addQuest(request):
    questForm = QuestionForm()
    result =questForm
    # result = '<div id="question">' \
    #          '<div class="form-group">' \
    #          '<label for="question">Question*</label>' \
    #          '<input type="text" class="form-control" id="question" placeholder="Write the question" maxlength="200" required>' \
    #          '</div>' \
    #             '<div class="form-group"> ' \
    #          '<label for="question">Answer*</label>' \
    #          '<input type="text" class="form-control" id="question" placeholder="Write the answer" maxlength="200" required>' \
    #          '</div>' \
    #          '<div class="form-group">' \
    #          '<label for="questDur">Question Duration: </label>' \
    #          '<select class="form-control" id="questDur">' \
    #          '<option value="1">1   min</option>' \
    #          '<option value="2">2   mins</option>' \
    #          '<option value="5">5   mins</option>' \
    #          '<option value="10">10 mins</option>' \
    #          '<option value="15">15 mins</option>' \
    #          '</select>' \
    #          '</div>' \
    #          '</div>'
    return HttpResponse(result)

class Report(APIView):
    def get(self,request,*args,**kwargs):
        data={
            "name":"John",
            'age':23
        }
        return Response(data)

