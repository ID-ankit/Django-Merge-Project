from django import forms

from .models import Post , User

# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('post_image','thumbnail','title', 'text','category','tags')
# authentication/forms.py



class UserSignUpForm(forms.ModelForm):
	username = forms.CharField(
		required=False,  # Make the username field optional
		widget=forms.TextInput(attrs={'placeholder': 'Username'}),
	
	)
		
	class Meta:
		model = User
		fields = ('first_name','username','password','ph_no','email','city','state','country','image',)


class UserloginForm(forms.ModelForm):
	username = forms.CharField(
	required=False,  # Make the username field optional
	widget=forms.TextInput(attrs={'placeholder': 'Username'}),)
	class Meta:
		model = User
		fields = ('username', 'password')


class ProfileForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['image', 'first_name','ph_no', 'address', 'city', 'state', 'country']
		
class EditProfileForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['image', 'first_name','ph_no', 'address', 'city', 'state', 'country']
