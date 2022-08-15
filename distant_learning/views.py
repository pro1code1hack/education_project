from django.shortcuts import render

from journal.models import GroupStudent, Grade
from .models import DistantLearningLesson


# Create your views here.

def distant_learning(request, grade=None):
    if grade:
        # get the group students for the given grade
        #TODO ask on the forum if it is possible to write this query in one line
        #TODO handle exceptions
        grade_id = Grade.objects.get(number=grade)
        group_students = GroupStudent.objects.filter(grade=grade_id)
        lessons = DistantLearningLesson.objects.get(group__in=group_students)
    else:
        lessons = DistantLearningLesson.objects.all()
        return render(request, 'distant_learning/distant_learning_all.html', {'lessons': lessons})
    return render(request, "distant_learning/distant_learning_group.html", {"lessons": lessons})
