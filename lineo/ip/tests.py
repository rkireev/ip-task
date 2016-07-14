from datetime import datetime

from django.test import TestCase, RequestFactory

from lineo.ip.models import Visit
from lineo.ip.views import ips

class VisitTestCase(TestCase):
    def setUp(self):
        Visit.objects.create(ip_address="123.123.123.123")

    def test_db(self):
        """Creatoin of a new object checking"""
        test_object = Visit.objects.get(ip_address="123.123.123.123")
        self.assertEqual(test_object.time.replace(second=0, microsecond=0),
                         datetime.now().replace(second=0, microsecond=0))

class RequestTestCase(TestCase):
    def setUp(self):
		self.factory = RequestFactory()

    def test_request(self):
        """Request processing check"""
        test_post = ips(self.factory.post('/ip'))
        test_get = ips(self.factory.get('/ip'))
        self.assertEqual(test_post.status_code, 201)
        self.assertEqual(test_get.status_code, 200)