from django_filters import FilterSet, DateFilter, CharFilter
from .models import Author, Category, Post, PostCategory, Comment
from django.forms import DateInput

 
 
# создаём фильтр
class PostFilter(FilterSet):
    dateCreation = DateFilter(lookup_expr='gt', label='Опубликовано после ', widget=DateInput(format='%d.%m.%Y', attrs={'type': 'date'}))
    author__authorUser__username = CharFilter(lookup_expr='iexact', label='Имя автора')
    title = CharFilter(lookup_expr='iexact', label='Наименование статьи')
    class Meta:
        model = Post
        fields = ('title', 'author__authorUser__username', 'dateCreation') # поля, которые мы будем фильтровать (т.е. отбирать по каким-то критериям, имена берутся из моделей)