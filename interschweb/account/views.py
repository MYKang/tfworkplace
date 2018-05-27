from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SignupForm
from django.contrib.auth.models import User



def signin(request):
	return render(request, 'account/login.html')

def signup(request):
	if request.method == "POST":
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.email = form.cleaned_data['email']
			user.phone = form.cleaned_data['phone']
			user.save()
			return HttpResponseRedirect('/')
		else:
			return render_to_response('account/error.html', {'form': form})
			# HttpResponse('회원가입이 정상적으로 되지 않았습니다.')
	else:
		form = SignupForm()
		return render(request, 'account/adduser.html', {'form':form})