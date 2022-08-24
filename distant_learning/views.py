from django.shortcuts import render

from journal.models import GroupStudent, Grade
from .models import DistantLearningLesson


# Create your views here.

def distant_learning_course(request, course: int = None):
    lessons = DistantLearningLesson.objects.filter(course=course)

    return render(request, "distant_learning/distant_learning_all.html", {"lessons": lessons})


def distant_learning_single(request, course: int = None, pk: int = None):
    lessons = DistantLearningLesson.objects.filter(course=course, pk=pk)
    print(lessons)
    return render(request, 'distant_learning/distant_learning_single.html', {'lessons': lessons})


def distant_learning_all_topics_course(request, course):
    lessons = DistantLearningLesson.objects.filter(course=course)
    print(lessons)
    return render(request, 'distant_learning/distant_learning_topics.html', {'lessons': lessons})
