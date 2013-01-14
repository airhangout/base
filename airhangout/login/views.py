# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import User
import md5
from django.template import RequestContext

def login(request):
	return render_to_response('login/login.html')

def loginResult(request):
	user_name = request.POST['username']
	pwd = request.POST['pwd']
	
	request.session['IsLogin'] = 0;
	m = md5.new()
	m.update(pwd)
	message = 'username or password is wrong'
	try:
		users = User.objects.get(username=user_name)
	except User.DoesNotExist:
		pass
	else:
		if(users.password == m.hexdigest()):
			message = u'%s, login now' % user_name
			request.session['IsLogin'] = 1;
			request.session['member_id'] = users.id;
			request.session['member_name'] = users.username
	
	return render_to_response('login/loginResult.html', {'username':message}, context_instance=RequestContext(request))
	
	
def register(request):
	return render_to_response('login/register.html')
	

def registerResult(request):
	user_name = request.POST['username']
	pwd = request.POST['pwd']
	repwd = request.POST['repwd']
	message = user_name
	request.session['IsLogin'] = 0;
	if(pwd != repwd):
		message = 'please enter same password'
	else:
		m = md5.new()
		m.update(pwd)
		try:
			users = User.objects.get(username=user_name)
		except User.DoesNotExist:
			p = User(username=user_name, password=m.hexdigest())
			p.save()
			request.session['IsLogin'] = 1
			request.session['member_id'] = p.id
			request.session['member_name'] = user_name
			
		else:
			message = "this user exists now"
	return render_to_response('login/loginResult.html', {'username':message}, context_instance=RequestContext(request))
	
def testSession(request):
	return HttpResponse(request.session['IsLogin'])