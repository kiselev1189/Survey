from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from .models import Survey
from .forms import ResponseForm

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
            return HttpResponseRedirect("/confirm/%s" % response.uuid)
    else:
        form = ResponseForm(survey=survey)
        print(form)

    return render(request, "survey_app/survey.html", {"response_form":form, "survey":survey})