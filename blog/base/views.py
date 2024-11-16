from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import (ListView, 
    DetailView, CreateView, UpdateView, 
    DeleteView)
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.utils.timesince import timesince

import json

from . import models
from . import forms

class HomeView(ListView):
    model = models.Post
    template_name = 'home.html'
    ordering = ['-post_date']

class PostDetailsView(DetailView):
    model = models.Post
    template_name = 'post_details.html'

    def get_context_data(self, **kwargs):
        stuff = get_object_or_404(models.Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context = super().get_context_data(**kwargs)
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context


class AddPostView(CreateView):
    model = models.Post
    form_class = forms.CreatePostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdatePostView(UpdateView):
    model = models.Post
    form_class = forms.EditPostForm
    template_name = 'update_post.html'

class DeletePostView(DeleteView):
    model = models.Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class AddCategoryView(CreateView):
    model = models.Category
    fields = '__all__'
    template_name = 'add_category.html'

def CategoryView(request, cats):
    category = models.Category.objects.get(name=cats.replace('-', ' '))
    category_posts = models.Post.objects.filter(category=category).order_by('-post_date')
    return render(request, 'categories.html', {'cats': category, 'category_posts': category_posts})

class CategoryListView(ListView):
    model = models.Category
    template_name = 'category_list.html'

def LikeView(request, pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            post = get_object_or_404(models.Post, pk=pk)
            if post.likes.filter(id=request.user.id).exists():
                post.likes.remove(request.user)
                liked = False
            else:
                post.likes.add(request.user)
                liked = True

            return JsonResponse({'liked': liked, 'like_count': post.likes.count()})
        else:
            return render(request, 'page_not_found.html')
    else:
        return redirect('register')

def AddCommentView(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(models.Post, id=pk)
        body = json.loads(request.body)

        if not body:
            print(body)
            return JsonResponse({'error': 'Comment body cannot be empty'}, status=400)

        comment = models.Comment.objects.create(post=post, author=request.user, body=body['body'])
        
        return JsonResponse({
            'comment': comment.body,
            'user': comment.author.first_name.title(),
            'created_on': timesince(comment.created_on),
        })
    return JsonResponse({'error': 'Only POST method is allowed'}, status=405)



class CreateProfilePageView(CreateView):
    model = models.Profile
    template_name = 'create_profile.html'
    form_class = forms.ProfileCreateForm

    def get_success_url(self):
        return reverse_lazy('profile')


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)