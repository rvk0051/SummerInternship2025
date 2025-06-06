"""
This module contains all the view classes for handling blog posts operations:
- Listing all posts (PostListView)
- Viewing individual posts (PostDetailView)
- Creating new posts (PostCreateView)
- Updating existing posts (PostUpdateView)
- Deleting posts (PostDeleteView)

The views implement proper authentication and authorization using Django's
LoginRequiredMixin and UserPassesTestMixin.

Dependencies:
    - Django's generic class-based views
    - Post model from models.py
    - Django authentication system
"""

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from ..models import Post


class PostListView(ListView):
    """
    Display all blog posts on the homepage.
    
    Attributes:
        model: Post model
        template_name: Path to template file
        context_object_name: Name used in template context
        ordering: Sort posts by creation date (newest first)
    
    Template context provides:
        - posts: QuerySet of all blog posts
    """
    model = Post
    template_name = 'blogging/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 10  # Add pagination for better performance


class PostDetailView(DetailView):
    """
    Display a single blog post with full content.
    
    Attributes:
        model: Post model
        template_name: Path to template file
    
    Template context provides:
        - post: Single Post object
        - author: User who wrote the post
    """
    model = Post
    template_name = 'blogging/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    Handle creation of new blog posts.
    
    Requires user authentication (LoginRequiredMixin).
    
    Attributes:
        model: Post model
        fields: Form fields for post creation
        template_name: Path to template file
    """
    model = Post
    fields = ['title', 'content']
    template_name = 'blogging/post_form.html'

    def form_valid(self, form):
        """Set the current user as the post author before saving."""
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Handle updates to existing blog posts.
    
    Requires:
        - User authentication (LoginRequiredMixin)
        - Author verification (UserPassesTestMixin)
    
    Attributes:
        model: Post model
        fields: Editable fields
        template_name: Path to template file
    """
    model = Post
    fields = ['title', 'content']
    template_name = 'blogging/post_form.html'

    def form_valid(self, form):
        """Verify author and save updates."""
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """
        Verify the current user is the post author.
        
        Returns:
            bool: True if user is author, False otherwise
        """
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Handle deletion of blog posts.
    
    Requires:
        - User authentication (LoginRequiredMixin)
        - Author verification (UserPassesTestMixin)
    
    Attributes:
        model: Post model
        template_name: Path to confirmation template
        success_url: Redirect target after successful deletion
    """
    model = Post
    template_name = 'blogging/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        """
        Verify the current user is the post author.
        
        Returns:
            bool: True if user is author, False otherwise
        """
        post = self.get_object()
        return self.request.user == post.author