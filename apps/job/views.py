from django.shortcuts import render
from .models import Job

def detail_job(request, job_id):
    job = Job.objects.filter(pk=job_id)

    return render (request, 'job/detail_job.html', {'job': job})

