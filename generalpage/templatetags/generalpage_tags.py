from django import template
from generalpage.models import *

register = template.Library()

@register.simple_tag(name = 'getjobs')
def get_jobs():
    return Jobs.objects.all()

@register.simple_tag(name = 'getjobs_by_id')
def get_jobs_by_id(id):
    return Jobs.objects.filter(pk = id)

@register.simple_tag(name = 'getskills')
def get_skills():
    return MySkills.objects.all()

@register.simple_tag(name = 'getprojects')
def get_skills():
    return Projects.objects.all()