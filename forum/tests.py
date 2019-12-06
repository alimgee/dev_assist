from django.test import TestCase
from django.contrib.auth.models import User
from forum.forms import QueryForm, CommentForm
from .models import Post, Comment
from django.shortcuts import get_object_or_404



# Tests to check the forum
class TestForumNotLoggedIn(TestCase):
    # testing loading of forum landing page
    def test_forum_landing_page(self):
        response = self.client.get('/community/')
        self.assertEqual(response.status_code, 200)

    # testing load of relevant templates to community page
    def test_forum_page_templates_load(self):
        response = self.client.get('/community/')
        self.assertTemplateUsed(response, "forum/forum_list.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "forum/includes/intro.html")

    # test load of add post to forum, requires login
    def test_add_post_to_forum_page_load(self):
        # user not logged in page should redirect
        response = self.client.get('/community/query/new/')
        self.assertEqual(response.status_code, 302)
    
    def test_post_view_one_not_logged(self):
        '''
        testing that view post detail can be viewed using 
        the views.query_detail function when a user is not logged in
        '''
        self.credentials = { 'username': 'testuser', 'password': 'secret'}
        User.objects.create_user(**self.credentials)
        ''' 
        creating test user (id will be 1), and test post (id also 1) 
        as a valid post is needed to test detail view
        '''
        post = Post(title = "post title", content="content here", author_id=1)
        post.save()
        response = self.client.get('/community/query/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "forum/post_detail.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "forum/includes/intro.html")
        self.assertTemplateUsed(response, "forum/includes/modals.html")
    

class TestForumLoggedIn(TestCase):
    # tests for when logged in

    # setting up logged in user
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
        self.client.post('/login/', self.credentials, follow=True)
    
    # test load of add post to forum, requires login
    def test_add_post_to_forum_page_load(self):
        # user logged in page should load
        response = self.client.get('/community/query/new/')
        self.assertEqual(response.status_code, 200)

    # test load of add post to forum, requires login
    def test_add_post_to_forum(self):
        response = self.client.get('/community/query/new/')
        self.assertTemplateUsed(response, "forum/post_form.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "forum/includes/intro.html")

    # testing add post form accepts valid data
    def test_post_form(self):
        form_data = {'title': 'djangotest',
        'content': 'this is a post',}
        form = QueryForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    # testing add comment form accepts valid data
    def test_post_form(self):
        form_data = {'title': 'djangotest',
        'content': 'this is a post',}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_correct_error_message_title(self):
        '''
        testing correct error message gets loaded
        when title field is not filled in on add
        post form
        '''
        form = QueryForm({"title": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["title"], [u"This field is required."])
    
    def test_correct_error_message_content(self):
        '''
        testing correct error message gets loaded
        when content field is not filled in on add
        post form
        '''
        form = QueryForm({"title": "title", 'content':""})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["content"], [u"This field is required."])
    
    def test_post_view_one(self):
        '''
        testing that when a post is added via form
        it can be viewed using the views.query_detail
        function
        '''
        user = User.objects.get(username='testuser')
        post = Post(title = "post title", content="content here", author_id=user.id)
        post.save()
        response = self.client.get('/community/query/{}/'.format(post.pk))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "forum/post_detail.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "forum/includes/intro.html")
        self.assertTemplateUsed(response, "forum/includes/modals.html")
    

    def test_edit_post_page_load(self):
        '''
        testing that when a post is added via form
        it can be edited and loaded using the views.edit_query
        function
        '''
        user = User.objects.get(username='testuser')
        post = Post(title = "post title", content="content here", author_id=user.id)
        post.save()
        response = self.client.get('/community/query/1/edit/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "forum/edit_form.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "forum/includes/intro.html")
        

  
        
        
        
    
   
