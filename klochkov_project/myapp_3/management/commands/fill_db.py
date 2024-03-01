from random import choice
from django.core.management.base import BaseCommand
from myapp_3.models import Author, Post

LOREM = "Клиент очень важен, за клиентом пойдет клиент. Но в то же время они происходили с большим трудом и болью. Если говорить до мельчайших подробностей, то никто не должен заниматься никакой работой, если не получит от нее какой-либо пользы. Не сердись на боль, на выговор, на удовольствие он хочет быть волоском от боли в надежде, что не будет размножения. Если они не ослеплены похотью, они не выйдут; виноваты те, кто оставляет свои обязанности и смягчает свои сердца, то есть свои труды."


class Command(BaseCommand):
    help = "Generate fake authors and posts."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        if count <= 0:
            self.stdout.write(self.style.ERROR('Count must be greater than 0'))
            return

        for i in range(1, count + 1):
            author = Author.objects.create(
                name=f'Author{i}', email=f'mail{i}@mail.ru')
            self.stdout.write(self.style.SUCCESS(
                f'Created author {author.name}'))

            for j in range(1, count + 1):
                post = Post.objects.create(
                    title=f'Title{j}',
                    content=f'{choice(LOREM)}',
                    author=author
                )
                self.stdout.write(self.style.SUCCESS(
                    f'Created post {post.title}'))
