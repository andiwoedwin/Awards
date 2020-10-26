
from django.test import TestCase
from .models import Post
from user.models import Profile
from django.contrib.auth.models import User
# Create your tests here.
class TestPost(TestCase):
    def setUp(self):
        self.user = User(username='Mabele')
        # self.user.save()
        self.post_test = Post(id=1,content='football is good', image='default.jpg', title='socker')

    def test_instance(self):
        self.assertTrue(isinstance(self.post_test, Post))
        
    def test_save_post(self):
        posts = Post.objects.all()

    def test_delete_post(self):
        before = Profile.objects.all()
        after = Profile.objects.all()
        self.assertTrue(len(before) == len(after))


