from .models import Member
import django_filters

class MemberFilter(django_filters.FilterSet):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', ]