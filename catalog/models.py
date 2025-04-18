from django.db import models


class Post(models.Model):
    content = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tag = models.ManyToManyField("Tag", related_name="posts")

    class Meta:
        ordering = ["-created_time", "is_done"]

    def __str__(self):
        return self.content


class Tag(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name
