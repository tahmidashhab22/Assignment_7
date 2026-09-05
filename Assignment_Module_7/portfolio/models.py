from django.db import models


# This is our Project model.
# Every project I add through the Django Admin will be saved
# in the database using these fields.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tech_used = models.CharField(
        max_length=200,
        help_text="Example: Python, Django, HTML, CSS"
    )
    github_link = models.URLField(
        max_length=300,
        blank=True,
        help_text="Link to the GitHub repo for this project (optional)"
    )
    image = models.ImageField(
        upload_to='project_images/',
        blank=True,
        null=True,
        help_text="Optional screenshot of the project"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    # This controls the order projects show up in (newest first)
    class Meta:
        ordering = ['-created_at']

    # This makes projects show up with their title (instead of "Project object (1)")
    # in the Django Admin list.
    def __str__(self):
        return self.title
