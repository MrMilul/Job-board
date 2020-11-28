from django.shortcuts import render, redirect
from .forms import AddJobForm
from .models import Job

def detail_job(request, job_id):
    job = Job.objects.filter(pk=job_id)

    return render (request, 'job/detail_job.html', {'job': job})


def add_job(request):
    if (request.method == 'POST'):
        form = AddJobForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()

            return redirect('dashboard')


    else:
        form = AddJobForm()

    return render(request, 'job/add_job.html', {'form':form})
