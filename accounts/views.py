from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login

from .forms import CustomUserCreationForm


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
			return redirect('notes_list')

	context = {'form': form}
	return render(request, 'signup.html', context)
