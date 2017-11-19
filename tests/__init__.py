from unittest import TestCase

import json
from .utils import FlaskTestCaseMixin

class ProjectTestCase(TestCase):
    pass


class ProjectAppTestCase(FlaskTestCaseMixin, ProjectTestCase):

    def _create_app(self):
        raise NotImplementedError

    def setUp(self):
        super(ProjectAppTestCase, self).setUp()
        self.app = self._create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        super(ProjectAppTestCase, self).tearDown()
        self.app_context.pop()