from django.shortcuts import render

# Create your views here.

# create a class-based view to display all lessons for the specific group
from django.views import View

from journal.models import GroupStudent, Grade
from lessons.models import Lesson

# def lesson_list(request, pk=None):
#     if pk:
#         group = GroupStudent.objects.get(pk=pk)
#         # lessons = Lesson.objects.filter(group=group)
#     lessons = Lesson.objects.all()
#     return render(request, 'lessons.html', {'lessons': lessons})

# write a function to display all lessons
from people.models import Teacher


# def lesson_list(request, grade=None):
#     lessons = Lesson.objects.all()
#     if grade:
#         # select the group with the given grade
#         group = GroupStudent.objects.get(grade__number=grade)
#         lessons = lessons.filter(group=group)
#         return render(request, 'lessons.html', {'lessons': lessons, 'group': group})
#     return render(request, 'lessons.html', {'lessons': lessons})

class LessonListView(View):
    def get(self, request, grade=None):
        lessons = Lesson.objects.all()
        if grade:
            # select the group with the given grade
            group = GroupStudent.objects.get(grade__number=grade)
            lessons = lessons.filter(group=group)
            return render(request, 'lessons.html', {'lessons': lessons, 'group': group})
        return render(request, 'lessons.html', {'lessons': lessons})

    def post(self, request, grade=None):
        pass
