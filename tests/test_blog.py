import unittest
from app.models import Comment, User, log
from app import db


class PitchModelTest(unittest.TestCase):
    def setUp(self):
        self.user_emma = User(
            username='emma', password='potato', email='emma@ms.com')
        self.new_blog = Blog(id=1, pitch_title='Test', pitch_content='This is a test blog',
                               category="interview", user=self.user_emma)

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.pitch_title, 'Test')
        self.assertEquals(self.new_blog.pitch_content, 'This is a test blog')
        self.assertEquals(self.new_blog.category, "interview")
        self.assertEquals(self.new_blog.user, self.user_emma)

    def test_save_pitch(self):
        self.new_blog.save_pitch()
        self.assertTrue(len(Blog.query.all()) > 0)

    def test_get_pitch_by_id(self):
        self.new_blog.save_pitch()
        got_pitch = Blog.get_blog(1)
        self.assertTrue(get_blog is not None)
