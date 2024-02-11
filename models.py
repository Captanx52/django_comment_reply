from django.db import models

class Comment(models.Model):
    post = models.ForeignKey("post", on_delete=models.CASCADE)
    text = models.TextField(max_length=512)

    def __str__(self):
        return'{}-{}'.format(self.pk, self.text)
class CommentAnswer(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    text = models.TextField(max_length=512)