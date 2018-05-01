from django.db import models


class SecurityManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().using("data_db").order_by("-event_timestamp")


class Security(models.Model):
    camera = models.IntegerField(blank=True, null=True)
    filename = models.CharField(max_length=80, blank=True, null=True)
    frame = models.IntegerField(blank=True, null=True)
    file_type = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()
    event_timestamp = models.DateTimeField()

    objects = SecurityManager()

    class Meta:
        managed = False
        db_table = 'security'
