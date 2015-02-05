import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):              # __unicode__ on Python 2
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):              # __unicode__ on Python 2
        return self.choice_text

'''
# Type of questions
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
    question_title = models.CharField( max_length = 100 )
    question_text = models.TextField()
    question_points = models.FloatField()
    question_type = models.CharField( max_length = 24, choices = question_types )

    # When this question was added
    add_date = models.DateTimeField( 'date added' )

    # Who added this question
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
