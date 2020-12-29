from django.shortcuts import render, redirect
from .forms import AddJobForm, ApplicationForm
from .models import Job, Application
from django.contrib.auth.decorators import login_required


def detail_job(request, job_id):
    job = Job.objects.filter(pk=job_id)

    return render (request, 'job/detail_job.html', {'job': job})

@login_required
def apply_for_job(request, id):
    job = Job.objects.get(pk=id)

    if request.method == "POST":
        form = ApplicationForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.created_by = request.user
            application.save()
            return redirect('dashboard')
    else:
        form = ApplicationForm()
        return render(request, 'job/apply_for_job.html', {'form': form, 'job': job})





























# def add_job(request):
#     if (request.method == 'POST'):
#         form = AddJobForm(request.POST)
# 
#         if form.is_valid():
#             job = form.save(commit=False)
#             job.created_by = request.user
#             job.save()
# 
#             return redirect('dashboard')
# 
# 
#     else:
#         form = AddJobForm()
# 
#     return render(request, 'job/add_job.html', {'form':form})
