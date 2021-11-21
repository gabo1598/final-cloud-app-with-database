from django.contrib import admin
# <HINT> Import any new Models here

from .models import Course, Lesson, Instructor, Learner , Choice, Question, Submission

# <HINT> Register QuestionInline and ChoiceInline classes here


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']
    
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('get_question', 'choice_text', 'is_correct')
    list_filter = ['is_correct']
    search_fields = ['choice_text']
    def get_question(self, obj):
        return obj.question.question_text
    get_question.short_description = 'Question'
    get_question.admin_order_field = 'question_text'


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question)
admin.site.register(Choice)
