from django.test import TestCase
from django.utils import timezone

from api.models import Security


class SecurityTestCase(TestCase):
    def setUp(self):
        Security.objects.create(
            camera=0,
            filename="filename",
            frame=0,
            file_type=0,
            timestamp=timezone.now(),
            event_timestamp=timezone.now()
        )

    def test_database_not_empty(self):
        self.assertEquals(Security.objects.all().count(), 1)

