from django.contrib import auth
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from prodigy.helpers.views import template

def login(request):
	return auth.views.login(request,
				template_name='accounts/login.html')

@template('accounts/register.html')
def register(request):
	next = request.REQUEST.get('next', '')
	if request.method == 'POST':
		form = auth.forms.UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					'%s?next=%s' % (reverse(login), next))
	else:
		form = auth.forms.UserCreationForm()
	return {'form': form, 'next': next}

def logout(request):
	return auth.views.logout(request,
				template_name='accounts/logged_out.html')

@template('accounts/permission_error.html')
def permission_error(request):
	return {'next': request.GET.get('next', '')}

# vim:set ft=python ts=4 sw=4 tw=79 noet: 
