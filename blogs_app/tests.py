from django.test import TestCase
from .models import Post

# Create your tests here.

class PostModelTesting(TestCase):

    def setUp(self):
        """Doing here setUp for perform testing like creating model instance.
           So than further we can test them.
        """


        self.titles = ('What is Django ?', 'Explain the architecture of Django ? ', "Explain Django-Rest-Framework ?")
        self.authors = ('Krishna', 'Aisha', 'Ankit')

        for i in range(3):
            title = self.titles[i]
            author = self.authors[i]
            slug   = title

            # creating object here
            Post.objects.create(title=title, author=author, slug=slug)

        print('\n SetUp Done Successfully')
    
    def test_post_instance(self):
        """Checking post instance here"""
        
        for i in range(3):
            author_name = self.authors[i]        
            post = Post.objects.get(author = author_name
                
            )
            self.assertTrue(isinstance(post, Post))
    
    def test_post_insertion(self):
        """Checking weather post is inserting successuly and all fields value coming accurately"""
        title = self.titles[0]
        author = self.authors[0]

        post1 = Post.objects.get(title=title)

        # checking like post author name is equal to self.author[0] or not
        self.assertEqual(post1.author, author)

        # checking slug here
        self.assertEqual(post1.slug, title )

        # checking author here
        self.assertEqual(post1.author, self.authors[0])

        print('\n Post Insertion test cases are passed successfully')

    def test_fetch_post(self):
        """In this we are going fetch our post from db using different fields such as: 
            pk, title, slug, author."""
        # fetching post using pk
        post = Post.objects.get(pk=1)
       
        #  fetch testing using valid pk 
        self.assertIsNotNone(obj=post)

        # fetching post using author
        author_post = Post.objects.get(author='Krishna')
        
        # tesing using author name weather post is exist
        self.assertIsNotNone(obj=author_post)

        # fetching using title
        title_post = Post.objects.get(title=self.titles[2])

        # testing via  title post
        self.assertIsNotNone(title_post)

        # fetching using post slug
        slug_post = Post.objects.get(slug=self.titles[1])

        # testing using post slg
        self.assertIsNotNone(obj=slug_post)


