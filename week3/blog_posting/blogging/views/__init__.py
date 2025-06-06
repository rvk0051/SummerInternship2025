from .post import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostDeleteView,
    PostUpdateView
)
from .authentication import (
    register,
    dashboard,
    edit_profile
)

__all__ = [
    register,
    dashboard,
    edit_profile,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostDeleteView,
    PostUpdateView
]
