from django.core.management.base import BaseCommand
from django.db import transaction
from myapp_2.models import Author, Post


class Command(BaseCommand):
    help = "Generate fake authors and posts."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int,
                            help='Number of authors and posts to generate')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        if count <= 0:
            self.stdout.write(self.style.ERROR('Count must be greater than 0'))
            return

        with transaction.atomic():
            for i in range(1, count + 1):
                author = Author.objects.create(
                    name=f'Name{i}', email=f'mail{i}@mail.ru')
                self.stdout.write(self.style.SUCCESS(
                    f'Created author {author.name}'))

                for j in range(1, count + 1):
                    post = Post.objects.create(
                        title=f'Title{j}',
                        content=f'Text from {author.name} #{j} is bla bla bla text.',
                        author=author
                    )
                    self.stdout.write(self.style.SUCCESS(
                        f'Created post {post.title}'))

        self.stdout.write(self.style.SUCCESS(
            f'Successfully created {count} authors and {count**2} posts'))
