from django.shortcuts import render

from .models import *
from .templatetags.generalpage_tags import *

networks = [
    'https://github.com/zakharfsk',
    'https://www.instagram.com/the_fiveteen',
    'https://t.me/zaharfsk',
    'https://www.linkedin.com/in/zakhar-fesik-a13569228'
]

def general(request):

    context =  {
        'title': 'zakharfsk',
        'networks': networks,
        'link_on_project': 'https://github.com/zakharfsk/my-resume#readme'
    }

    return render(
        request,
        'generalpage/index.html',
        context
    )


def expirienceJobs(request):

    context =  {
        'title': 'Досвід роботи',
        'networks': networks
     }

    return render(
        request,
        'generalpage/jobs.html',
       context
    )


def select_jobs(request, job_id):
    return render(
        request,
        f'sitejob/job{job_id}.html',
        {'title': f'{get_jobs_by_id(job_id)[0]}'}
    )


def mySkills(request):

    context = {
        'title': 'Мої навички',
        'networks': networks
    }

    return render(
        request,
        'generalpage/myskills.html',
        context
    )

def myProjects(request):

    context = {
        'title': 'Мої проекти',
        'networks': networks
    }

    return render(
        request,
        'generalpage/myprojects.html',
        context
    )

def pageNotFound(request, exception):
    return render(request, 'generalpage/error404.html')


# def internalServerError(request, exception):
    # return render(request, 'generalpage/error404.html')
