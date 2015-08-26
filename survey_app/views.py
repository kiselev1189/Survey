from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from .models import Survey, UserProfile
from .forms import ResponseForm, UserForm

def index(request):
    survey_list = Survey.objects.all()
    context = {"survey_list":survey_list}
    return render(request, 'survey_app/index.html', context)

def survey_detail(request, survey_id):
    survey = Survey.objects.get(id=survey_id)
    if request.method == 'POST':
        form = ResponseForm(request.POST, survey=survey)
        if form.is_valid():
            response = form.save()
            return HttpResponseRedirect("/index.html")
    else:
        form = ResponseForm(survey=survey)
        print(form)

    return render(request, "survey_app/survey.html", {"response_form":form, "survey":survey})

def register(request):

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = UserProfile()
            profile.user = user

            profile.save()

            return HttpResponseRedirect("/index.html")

        else:
            print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request, "survey_app/register.html", {"user_form": user_form})