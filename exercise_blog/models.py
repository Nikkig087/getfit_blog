from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = ((0, "Not Published"), (1, "Published"))

class Exercise(models.Model):
    id = AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    instructions = models.TextField()
    benefits = models.TextField()
    instructor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="exercise_blog_post"
    )#was author =
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.instructor}"

class Comment(models.Model):
    id: AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    comment = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =["created_on"]
    def __str__(self):
        return f"Comment {self.comment} by {self.user}"

