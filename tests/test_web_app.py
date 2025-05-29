# test_web_app.py

import os
os.environ['DATABASE_URL'] = 'sqlite://'

from app import app, db
import unittest


class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app_ctxt = self.app.app_context()
        self.app_ctxt.push()
        db.create_all() # < --- update

    def tearDown(self):
        db.drop_all() # < --- update
        self.app_ctxt.pop()
        self.app = None
        self.app_ctxt = None

    def test_app(self):
        assert self.app is not None
        assert app == self.app
