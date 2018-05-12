from .models import Member
from .models import Student
import django_filters

class MemberFilter(django_filters.FilterSet):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', ]

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', ]