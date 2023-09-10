from django.shortcuts import render,redirect
from .models import Tasks

# Create your views here.

def home(request):
	task=Tasks.objects.all()


	return render(request,"task/home.html",{'task':task})

def task_add(request):
	if request.method =='POST':
		print("ASHISH")
		# retreive the user input
		tasks_id=request.POST.get("task_id")
		tasks_title=request.POST.get("task_title")
		tasks_descripation=request.POST.get("task_descripation")
		


		# create an object for model
		t=Tasks()
		t.id=tasks_id
		t.title=tasks_title
		t.descripation=tasks_descripation
		

		t.save()
		return redirect("/task/home")



	return render(request,"task/add_task.html",{})

def delete_task(request,title):
	t=Tasks.objects.get(pk=id)
	t.delete()

	return redirect("/task/home")


def update_task(request,title):
	task=Tasks.objects.get(pk=id)
	return render (request,"task/update_task.html",{'task':task})

	