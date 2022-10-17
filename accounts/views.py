from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt

from .forms import CustomUserCreationForm
from notes.models import Tag


# class SignUpView(CreateView):
# 	form_class = CustomUserCreationForm
# 	success_url = reverse_lazy('login')
# 	template_name = 'signup.html'


def sign_up_view(request):
	form = CustomUserCreationForm()

	if request.method == "POST":
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)

			current_user = request.user
			Tag.objects.create(name="General", user=current_user).save()

			return redirect('notes_list')

	context = {'form': form}
	return render(request, 'signup.html', context)
