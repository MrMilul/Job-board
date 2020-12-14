from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.job.forms import AddJobForm
from apps.job.models import Job


@login_required
def dashboard(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = AddJobForm()
            userprofile = request.user.userprofile
            context = {
                'userprofile': userprofile,
                'form': form
                }

            return render(request, 'userprofile/dashboard.html', context)
        else:
            up = Job.objects.get(pk=id)
            form = AddJobForm(instance=up)
            context = {
                'userprofile': request.user.userprofile,
                'form': form
            }
            return render(request, 'userprofile/dashboard.html', context)

    else:
        if id == 0:
            form = AddJobForm(request.POST)

            if form.is_valid():
                job = form.save(commit=False)
                job.created_by = request.user
                job.save()
                return redirect('dashboard')
        else:
            up = Job.objects.get(pk=id)
            form = AddJobForm(request.POST, instance=up)

            if form.is_valid():
                job = form.save(commit=False)
                job.created_by = request.user
                job.save()
                return redirect('dashboard')


def delete_job(request, id):
    if request.method == "POST":
        up = Job.objects.get(pk=id)
        up.delete()
        return redirect('dashboard')