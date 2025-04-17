from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.

from .models import Post

class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@email.com',
            password='secret',
        )
        cls.post = Post.objects.create(
            author=cls.user,
            title = 'A good title',
            body = 'Nice body of a post',
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, 'testuser')
        self.assertEqual(self.post.title, 'A good title')
        self.assertEqual(self.post.body, 'Nice body of a post')
        self.assertEqual("A good title", str(self.post))
