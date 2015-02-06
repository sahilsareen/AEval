from django.contrib import admin

# Register your models here.
from interview.models import Question, Choice, InterviewTestQuestion

def make_new_test(modeladmin, request, queryset):
    current_test_questions_ids = [i.interview_question_id for i in InterviewTestQuestion.objects.all()]
    
    for obj in queryset:
        if obj.id not in current_test_questions_ids:
            # Don't add a question twice
            q_id = InterviewTestQuestion(interview_question_id=obj.id)
            q_id.save()

make_new_test.short_description = "Add to interview test questions"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_title']}),
        (None,               {'fields': ['question_type']}),
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    list_display = ('question_title', 'question_type', 'question_text', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_title','question_text','question_type']
    actions = [make_new_test]

'''
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 2
'''

class InterviewTestQuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['interview_question']}),
        (None,               {'fields': ['score']}),
        ]

    list_display = ('interview_question','score','question_category')
#    list_display = ('interview_question','score')
    

admin.site.register(Question, QuestionAdmin)
admin.site.register(InterviewTestQuestion, InterviewTestQuestionAdmin)
