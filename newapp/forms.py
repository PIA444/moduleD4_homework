from django.forms import ModelForm
from django.shortcuts import redirect
from .models import Post
 
 
# Создаём модельную форму
class PostForm(ModelForm):
    # в класс мета, как обычно, надо написать модель, по которой будет строиться форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = Post
        fields = ['author', 'categoryType', 'postCategory', 'title', 'text']

        