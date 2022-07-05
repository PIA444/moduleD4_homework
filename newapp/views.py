from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Author, Category, Post, PostCategory, Comment
from .filters import PostFilter
from .forms import PostForm


class PostsList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-id')
    paginate_by = 10

class PostList(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

class PostsSearch(ListView):
    model = Post
    template_name = 'news_search.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-id')

    def get_context_data(self, **kwargs): # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset()) # вписываем наш фильтр в контекст
        return context

class CreatePost(CreateView):
    template_name = 'create_post.html'
    form_class = PostForm

# дженерик для редактирования объекта
class UpdatePost(UpdateView):
    template_name = 'create_post.html'
    form_class = PostForm
 
    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)
 
 
# дженерик для удаления товара
class DeletePost(DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'