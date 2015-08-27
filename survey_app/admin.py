from django.contrib import admin
from survey_app.models import Survey, Response, Question, AnswerText
# Register your models here.

class QuestionInline(admin.TabularInline):
    model = Question

class AnswerTextInline(admin.StackedInline):
    model = AnswerText
    fields = ("question", "body")
    readonly_fields = ("question",)

class SurveyAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


class ResponseAdmin(admin.ModelAdmin):
    inlines = [AnswerTextInline]
    readonly_fields = ("survey", "created", "updated", "uuid")


admin.site.register(Survey, SurveyAdmin)

admin.site.register(Response, ResponseAdmin)