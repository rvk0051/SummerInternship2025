from django.db import models
class Post(models.Model):
    title = models.CharField(max_length=200)  # Title of the blog post
    content = models.TextField()               # Content of the blog post
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the post was created
    updated_at = models.DateTimeField(auto_now=True)      # Timestamp when the post was last updated
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # Relationship with the User model
    class Meta:
        ordering = ['-created_at']  # Order posts by creation date, newest first
    def __str__(self):
        return self.title  # Return the title of the post when the object is printed
'''
Class Definition: The Post class defines a model for blog posts.

Fields:
# title: A CharField with a maximum length of 200 characters.
# content: A TextField for the main content of the post.
# created_at: A DateTimeField that automatically sets the timestamp when the post is created.
# updated_at: A DateTimeField that automatically updates the timestamp whenever the post is modified.
# author: A ForeignKey that creates a many-to-one relationship with the built-in User  model,
          allowing you to associate each post with an author.

Meta Class: The Meta class specifies that the posts should be ordered by the created_at field in descending order.

String Representation: The __str__ method returns the title of the post, which is useful 
                       for displaying the object in the Django admin interface or when printing.
'''

# Once, models are defined, we can interact with them using Django's ORM.
# Some common operations:

# Creating a New Record:
post = Post(title="My First Post", content="This is the content of my first post.", author=user)
post.save()  # Save the post to the database

# Querying Records:
all_posts = Post.objects.all()  # Retrieve all posts
first_post = Post.objects.get(id=1)  # Retrieve a post by its ID

# Updating Records
post.title = "Updated Title"
post.save()  # Save the changes to the database

# Deleting a Record:
post.delete() # Delete the post from the database