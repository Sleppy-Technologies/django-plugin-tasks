from django.conf import settings
from django.test import TestCase
from django_tasks.backends.database.models import DBTaskResult


class TestDjangoPluginTasks(TestCase):
    def test_installed_apps_injected(self):
        self.assertIn("django_tasks", settings.INSTALLED_APPS)
        self.assertIn("django_tasks.backends.database", settings.INSTALLED_APPS)

    def test_task_settings(self):
        self.assertEqual(
            settings.TASKS["default"]["BACKEND"],
            "django_tasks.backends.database.DatabaseBackend",
        )

    def test_task_models_exist(self):
        self.assertEqual(DBTaskResult.objects.count(), 0)
