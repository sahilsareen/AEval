import datetime

from django.db import models
from django.utils import timezone


# Type of questions
question_types = (
    ( "array", "Arrays" ),
    ( "linked_list", "Linked Lists" ),
    ( "hash_map", "Hash Maps" ),
    ( "stack", "Stacks" ),
    ( "queue", "Queues" ),
    ( "tree", "Trees" ),
    ( "graph", "Graphs" ),
    ( "heap", "Heaps" ),
    ( "trie", "Tries" ),
    ( "networking", "Computer Networking" ),
    ( "os", "Operating Systems" ),
    ( "general", "General Questions" ),
    )

class Question(models.Model):
    question_type = models.CharField( max_length = 24, choices = question_types, default = "general"  )
    question_title = models.CharField(max_length=50, default = 'notitle' )
    question_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField( 'date published' )

    def __str__(self):              # __unicode__ on Python 2
        return self.question_text

    def get_question_category(self):
        return self.question_type

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    correct = models.BooleanField( default = False )

    def __str__(self):              # __unicode__ on Python 2
        return self.choice_text

class InterviewTestQuestion(models.Model):
    # Add only the questionIds here
    interview_question = models.ForeignKey(Question)
    
    score = models.IntegerField( default = 1 )

    def question_text(self):
        return Question.objects.all()[self.interview_question.id].question_text

    def question_category(self):
        return str(Question.objects.all()[self.interview_question_id -1].get_question_category())

    question_category.admin_order_field = 'category'
    question_category.boolean = False
    question_category.short_description = 'Category'
        
#    def __str__(self):              # __unicode__ on Python 2
#        return self.question_id

'''
# XXX: Need to add support for these
# The database already supports mcqs with multiple answers
# Need to integrate an online judge for coding_questions
question_types = (
    ( "mcq", "Multiple Choice Question" ),
    ( "code", "Coding Question" ),
    )

# Languages allowed for coding questions
languages_supported = (
    ( "python", "Python" ),
    ( "c++", "C++" ),
    )

# --- All the questions go here ---
class Question( models.Model ):
    # The question
    # For now all questions carry the same weightage
    question_points = models.FloatField()

    # Who added this question
    # Might be useful for people who want to ask questions they made up 
    # for interviews and not use those put up by others
    user_name = models.CharField( max_length = 20 )

    # The correct answer for mcqs
    # XXX: Be sure this isn't the same as candidate_choice
    correct_answer = models.IntegerField( default = -2 )


# --- Candidates answers go here ---
class Choice(models.Model):
    # For which question
    question = models.ForeignKey( Question )

    # Maximum points for this question
    question_value = models.FloatField( default = 0.0 )

    # Candidate's answer for the question
    candidate_choice = models.IntegerField( default = -1 )
    candidate_choice_correct = models.BooleanField( default = False )
'''
