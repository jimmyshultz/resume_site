from django.db import models

class Category(models.Model):
    """Catergories to organize blog posts."""
    title = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        """Return a string representation of the model."""
        return self.title

class BlogPost(models.Model):
    """A blog post made by the admin."""
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=15_000)
    date_added = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)

    class Meta:
        ordering = ['-date_added',]

    def __str__(self):
        """Return a string representation of the model."""
        return self.title

class Comment(models.Model):
    """A comment on a blog post."""
    text = models.TextField(max_length=2_000)
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) <= 50:
            return f"{self.name} - {self.text}"
        else:
            return f"{self.name} - {self.text[:50]}..."
