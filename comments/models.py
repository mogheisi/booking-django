from django.db import models
from django.conf import settings


class AbstractComment(models.Model):
    CREATED = 1
    APPROVED = 2
    REJECTED = 3
    DELETED = 4
    STATUS_CHOICES = (
        (CREATED, 'Created'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
        (DELETED, 'Deleted')
    )
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    comment_body = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='%(class)ss')
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=1)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
