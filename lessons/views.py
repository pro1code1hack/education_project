from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.

# create a class-based view to display all lessons for the specific group
from django.views import View

from journal.models import GroupStudent, Grade
from lessons.models import Lesson, LessonImages, AdditionalFiles, LessonVideos

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
        lessons = Lesson.objects.all()  # get all lessons on the main page
        all_groups = GroupStudent.objects.all()  #
        if grade:
            try:
                group = GroupStudent.objects.get(grade__number=grade)
                lessons = lessons.filter(group=group)
            except GroupStudent.DoesNotExist or Lesson.DoesNotExist:
                return redirect('/404')
            return render(request, 'lessons/lessons.html', {'lessons': lessons,
                                                            'group': group,
                                                            'all_groups': all_groups})
        return render(request, 'lessons/lessons.html', {'lessons': lessons,
                                                        'all_groups': all_groups})


def get_lesson(request, pk=None):
    try:
        lesson = Lesson.objects.get(pk=pk)
        videos = LessonVideos.objects.select_related('lesson').filter(pk=pk)
        images = LessonImages.objects.select_related('lesson').filter(pk=pk)
        additional_files = AdditionalFiles.objects.select_related('lesson').filter(pk=pk)
    except Lesson.DoesNotExist:
        return redirect('/')
    return render(request, 'lessons/lesson.html', {"lesson": lesson,
                                                   'images': images, 'videos': videos,
                                                   "additional_files": additional_files,
                                                   })
