from django.core.management.base import BaseCommand
from blogapp.models import Category, Post, Tag


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            Post.objects.all().delete()
            Tag.objects.all().delete()
            Category.objects.all().delete()
            print("Data base cleared.//")
        except Exception as e:
            print(e.__str__())
