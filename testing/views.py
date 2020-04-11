from django.shortcuts import render,redirect
from .forms import ProfileForm,UserForm
from django.contrib import messages

from django.contrib.auth.models import User
# Create your views here.

def sample(request):
	if request.method == 'POST':
		user_form = UserForm(request.POST, instance=request.user)
		profile_form = ProfileForm(request.POST,request.FILES, instance=request.user.profile)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, 'sample.html',('Your profile was successfully updated!'))
			return redirect('sample')
		else:
			messages.error(request, 'sample.html',('Please correct the error below.'))
	else:
		user_form = UserForm(instance=request.user)
		profile_form = ProfileForm(instance=request.user.profile)
	return render(request, 'sample.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
def viewimage(request):
	
	imgview = User.objects.all().select_related('profile')
	return render(request,'imageview.html',{'imgview':imgview})
    	
    

        
        
        	
    
    	
    

        
            
            
            
            
        
            
    
        
        
       