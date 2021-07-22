from django.contrib import admin
from django.urls import path
from interviewers import views
from iommi import Table
from .models import Job , Applicants

urlpatterns = [
    path('', views.home,name="home"),
    path('dashboard', views.dashboard, name="dashboard"),

    path('interview/create', views.addInterview,name="add_interview"),
    path('interview', views.allInterviews, name="interviews"),
    path('interview/<int:interview_id>', views.interview, name="interview"),
    path('interview/<int:interview_id>/delete', views.interviewDelete, name="delete_interview"),
    path('interview/<int:interview_id>/addquestion', views.addQuestions, name="addInterQues"),
    path('interview/<int:interview_id>/question/<int:question_id>/delete', views.questDelete, name="delete_question"),

    # path('addQues', views.addQuest, name="add_question"),

    path('job/create', views.addJob, name="add_job"),
    path('job',views.Jobs,name="jobs"),
    path('job/<int:job_id>', views.eachJob, name="job"),
    path('job/<int:job_id>/delete', views.jobDelete, name="delete_job"),



    #INTERVIWEE PART
    path('startinterview/<int:applicant_id>', views.onlineInterview, name="interviewee_interview"),
    path('view/', views.dynamic_stream, name="videostream"),
    path('upload', views.upload, name="video"),
    path("record",views.record,name="recordvideo")
    # path(r'^/(?P<stream_path>(.*?))/$',views.dynamic_stream,name="videostream"),
    # path(r'^stream/$',views.indexscreen),


    # path('job/edit', views.jobEdit, name="edit_job")
    # path('boards/<int:board_id>/topics/<int:topic_id>/posts/<int:post_id>/edit', views.editPost.as_view(),
]
