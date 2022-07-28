import os.path

from django.core.management.base import BaseCommand
from blogapp.models import Category, Post, Tag


class Command(BaseCommand):
    def handle(self, *args, **options):

        Fillers = {
            'category': ['Экономика', 'Наука', 'Юмор'],
            'tag': ['Мир', 'Спад', 'Рак', 'Изобретения', 'StandUp', 'КВН'],
            'post': [
                {'name': 'Мировая экономика лежит в луже грязи',
                 'category': 'Экономика',
                 'tags': ['Мир', 'Спад']
                 },
                {'name': 'Ученые изобрели радикальное лечение рака',
                 'category': 'Наука',
                 'tags': ['Рак', 'Изобретения']
                 },
                {'name': 'КВН и вправду устарел. Стенд-Апы вошли в моду',
                 'category': 'Юмор',
                 'tags': ['StandUp', 'КВН']
                 },
            ],
        }

        # categories = Category.objects.all()
        # print(categories)
        # print(type(categories))
        # for cat in categories:
        #     print(cat)
        #     print(type(cat))
        #
        # category = Category.objects.get(name='Фрукты')
        # print(category)
        # categories = Category.objects.filter(name='Фрукты')
        # for cat in categories:
        #     print(cat)
        #
        # post = Post.objects.first()
        # print(post)
        # print(type(post))
        # print(post.category)
        # for t in post.tags.all():
        #     print(t)
        #
        # Category.objects.create(name='Новая категория', desc='Описание')
        # category = Category.objects.get(name='Новая категория')
        # category.name = 'Овощи'
        # category.save()
        # category.delete()
        #
        # try:
        #     category = Category.objects.get(name='Овощи')
        # except BaseException as e:
        #     print(e.__str__())
        # except Exception as e:
        #     print("Simple exception: ", e.__str__())
        # print("DB Filled.//")

        #filling categories
        for category_name in Fillers['category']:
            try:
                Category.objects.create(name=category_name, desc='Описание')
            except Exception as e:
                print("Error while category filling: ", e.__str__())
        #filling tags
        for tag_name in Fillers['tag']:
            try:
                Tag.objects.create(name=tag_name)
            except Exception as e:
                print("Error while tag filling: ", e.__str__())
        #filling posts
        for post in Fillers['post']:
            try:
                Post.objects.create(name=post['name'], text='Sample text',
                                    category=Category.objects.get(name=post['category']),
                                    )
                cur_post = Post.objects.get(name=post['name'])
                #cur_post.category = Category.objects.get(name=post['category'])
                cur_post.tags.set([Tag.objects.get(name=tag) for tag in post['tags']])
                cur_post.save()
            except Exception as e:
                print("Error while Post filling: ", e.__str__())
