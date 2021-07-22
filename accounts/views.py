from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as authlogin
from django.views.generic import TemplateView
from django.contrib import messages
from interviewers.models import Companies
from django.contrib.auth.models import User
from .forms import SignupForm, NewCompanyForm
# Create your views here.
#
# def signup(request):
#     signup = SignupForm(prefix="signup")
#     newcomp = NewCompanyForm(prefix="newcomp")
#     if request.method == "POST":
#         signup = SignupForm(request.POST, prefix="signup")
#         newcomp = NewCompanyForm(request.POST, prefix="newcomp")
#         if signup.is_valid() and newcomp.is_valid():
#             user = signup.save()
#             company = newcomp.save()
#             return redirect("home")
#     return render(request,'signup.html',{'signup':signup,'newcomp':newcomp})

class AddCommentView(TemplateView):

    signup = SignupForm
    newcomp = NewCompanyForm
    template_name = 'signup.html'

    def post(self, request):
        post_data = request.POST or None
        signup_form = self.signup(post_data, prefix='signup')
        newcomp_form = self.newcomp(post_data, prefix='newcomp')

        context = self.get_context_data(signup_form=signup_form,
                                        newcomp_form=newcomp_form)

        if signup_form.is_valid() and newcomp_form.is_valid():
            self.form_save(signup_form)
            self.form_save(newcomp_form)
            # company = Companies.objects.last()
            # user = User.objects.last()
            # company.companies.add(user)
            return redirect("dashboard")

        return self.render_to_response(context)

    def form_save(self, form):
        obj = form.save()
        messages.success(self.request, "{} saved successfully".format(obj))
        return obj

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)