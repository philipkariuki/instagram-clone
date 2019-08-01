from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Image,Profile,tags


class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.picha= Image(image_name = 'Picha', caption ='hii ni picha nzuri' )
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.picha,Image))

    # Testing Save Method
    def test_save_method(self):
        self.picha.save_image()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)




class ProfileTestClass(TestCase):
         
    def setUp(self):
        self.pablo = Profile(profile_name='pablo', bio='hii ni bio')

    def test_instance(self):
        self.assertTrue(isinstance(self.pablo, Profile))

    def tearDown(self):
        Profile.objects.all().delete()
        
    def test_save(self):
        self.pablo.save_profile()
        
    
class TagTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.pablo= tags( name = 'thetags' )
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.pablo,tags))
        
    # Testing Save Method
    def test_save_method(self):
        self.pablo.save_tag()