import django_filters
from .models import *

class FilterEmployeeInfo(django_filters.FilterSet):
    class Meta:
        model=Employee
        fields=['eid','ename']