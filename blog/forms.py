from django import forms
from .models import Post

class PostForm(forms.ModelForm):  #PostForm is the name of our Form

	class Meta:
		model = Post
		fields = ('title', 'text',)