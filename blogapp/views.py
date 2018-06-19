from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from . import forms
from blogapp.models import Post, Comment
from blogapp.forms import PostForm, CommentForm
# from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.


class AboutView(TemplateView):
    template_name = 'about.html'


class PostView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blogapp/post_detail.html'
    form_class = PostForm
    model = Post


class UpdatePostView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blogapp/post_detail.html'
    form_class = PostForm
    model = Post


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


class DraftListView(LoginRequiredMixin, ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')


class SignUp(CreateView):
    form_class = forms.SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('post_list')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})


def add_comment_to_post(req, pk):
    post = get_object_or_404(Post, pk=pk)
    if req.method == 'POST':
        form = CommentForm(req.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(req, 'blogapp/comment_form.html', {'form': form})


@login_required()
def comment_approval(req, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required()
def comment_delete(req, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)


@login_required()
def publish_post(req, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)
