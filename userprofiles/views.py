from django.shortcuts import render

from django.views.generic import CreateView

from .models import UserProfile

class UserCreateView(CreateView):
	model = UserProfile
	template_name = 'userprofiles/user_create.html'
	success_url = '/'
	form_class = 'UserForm'

	def form_valid(self, form):
		form.save()
		return super(UserCreate, self).form_valid(form)