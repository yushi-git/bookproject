from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings


User = get_user_model()

class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username='my_book_project_name').exists():
            User.objects.create_superuser(
                username='my_book_project_name',
                email='',
                password='my_book_project_password'
            )