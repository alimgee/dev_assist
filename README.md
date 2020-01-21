
<h1  align="center">
<a  href="https://dev-assist.herokuapp.com/"  target="_blank"><img  src="/documentation/desktop.gif"  alt="DevAssist Desktop Screen"/></a>
<a  href="https://dev-assist.herokuapp.com/"  target="_blank"><img  src="/documentation/mobile.gif"  alt="DevAssist Mobile Screen"/></a>
</h1>
<h2  align="center">
DevAssist
</h2>
<div  align="center">

  

This is project is part of the 'Full Stack Dev Milestone Project 4' module of the Code Institute Full Stack Software Development course, and is the final project of the course. The website intends to mimic a forum type environment where registered users can raise technical queries and respond to other users queries, with an ecommerce option to donate funds to the site creators. Python, Django, Bootstrap and Stripe technologies will be used to achieve this. The marks from this project contribute to the receipt of a diploma level award. The site can be accessed from https://dev-assist.herokuapp.com/
<br>
This site is purely for educational purposes only and does not provide any services. Do not enter personal information. The Ecommerce backend uses the test version of Stripe and will only work using the test stripe credit card number 4242424242424242, see https://stripe.com/docs/testing for test card details.

<br>
</div>

  

## Table of Contents

1.  [**UX**](#ux)
-  [**Project Goals**](#project-goals)
-  [**User goals**](#user-goals)
-  [**User Stories**](#user-stories)
-  [**Design**](#design)
-  [**Wireframes**](#wireframes)

  
2.  [**Features**](#features)
-  [**Existing Features**](#existing-features)
-  [**Future Features**](#future-features)
3.  [**Database**](#database)
4.  [**Technologies used**](#technologies-used)
5.  [**Testing**](#testing)
6.  [**Coding Notes**](#coding-notes)
7.  [**Deployment**](#deployment)
8.  [**Acknowledgements**](#acknowledgements)
9.  [**Disclaimer**](#disclaimer)

  
# UX

  

## Project Goals

The aim of this project is to create a Full Stack web app to fully demonstrate the learnings throughout the course. A pass in this project is required to pass the course and obtain certification. The site will use Python and the Django Framework with a back-end db (PostgreSQL) for the back-end stack. Bootstrap 4 and HTML will be used on the front-end stack. <br>
The site will mimic an open community support site for development type issues, with the community itself providing the support for other users on the site. Users will be be required to register on the site to add posts or comments. There will also be a donation functionality to demonstrate the use of eCommerce, in this case i will be using Stripe as a payment system. Registered Users will be able to donate small sums which will help keep the site maintained and also allow further future functionalities.
<br>


### User goals

User goals in brief are as follows:

1. To allow users to register on the site.
2. To allow users to Post a query or comment to the site when logged in.
3. To allow users to edit or delete their Posts
4. To  allow users to submit donations to the site management team to help assist with site maintenance and future additional functionalities

  

### User Stories
1.  I want to see a brief  summary of the main site sections and  relevant links when i go to the landing page of the site.
2. I want to be able to view my Posts on the site.
3. I want to be able to view Posts by other users to the site.
4.  I want Post per page to be limited to a small amount with the ability to view all reviews through pagination.
5.  Summary of Posts on the community page should have button links to the full Post.
6.  The full Post view should show the original user who created the Post.
7.  The full Post view should show the date of the Post.
8.  The full Post view should allow logged in users to edit or delete their own Posts.
9.  The full Post view should allow any logged in user to add a comment.
10.  The full Post view should show all comments associated with the Post.
11.  There should be an option to register on the site.
12. There should be an option to log onto the site.
13. There should be an option to log out of the site when logged in
14. I want to be able to send a donation to the site via a credit card payment option.
15. I want there to be a cart functionality where i can see what i have added to the cart for the current logged in session.
16. The cart will persist only during the logged in session.
17. There should be a checkout option on the cart page which clicks through to the order form payment screen.
18. The order form checkout page will sumarise the order and show the total payment.
19. The user will be able to add the credit card details and submit the payment with a valid card number(for the purpose of this project this will only be the Stripe test card number).
20. Successful payment will be messaged and the cart cleared on successful submit.
21. I should be able to search through the community posts.



## Design

  
**Fonts**

I decided to use the 'Ubuntu' font from google("[https://fonts.googleapis.com/css?family=Ubuntu](https://fonts.googleapis.com/css?family=Ubuntu)") as i felt that it was an 'easy on the eye' font and aided reading the Posts and comments.


**Colours**


![#757575](https://placehold.it/15/757575/000000?text=+) ***#757575*** ![#a8a9ad](https://placehold.it/15/a8a9ad/000000?text=+) ***#a8a9ad***  ![#fafafa](https://placehold.it/15/fafafa/000000?text=+) ***#fafafa***  
Initially i toyed with the idea of using a 70s style pallet as i found some of the colour schemes of this era interesting. However, once i started doing the project I began to think about using a monochrome style, trying to see if I can make a site looking interesting as possible with a bare minimum of colour.

**Topography**

The site uses bootstrap 4 to be fully responsive across multiple devices. It has been checked on multiple devices using chrome dev tools and physically on Chrome and Firefox on Desktop and a Samsung Galxay S9.The top navigation floats to the right on desktop size windows and collapses down to a drop-down navigation on mobile devices

## Wireframes

WIreFames were created using balsamiq tool with license key provided by the Code Institute. https://balsamiq.com/ and can be found in the  [/documentation ](/documentation) folder at  [/documentation/DevAssist_WireFrames.pdf](/documentation/DevAssist_WireFrames.pdf) .  The wireframes were created at the very start of the project on a notepad and later transferred. Throughout development there was a little scope change,  i adjusted the layouts as appropriate to the projects end goals, there were also new pages added to accommodate journeys not initially thought of that became needed as the project progressed.

  

## Features

### Existing Features

1. User can register and log on to the site.
2. User can view Posts
3. Registered in users can add/ delete / edit  Posts
4. Registered users can add comments on Posts
5. Registered users can make donations to the site using a Stripe based payment system.


### Future Features

Future versions of the project may have the following:

1. Images and code blocks to be uploaded.
2. WYSIWIG editors added to Posts.
3. A possible dev team to assist paid users.

 

# Database

The project uses django so the development environment uses dbsqlite database, for production I am using a postgres database.

### Database schema

My schema was initially written down in a notebook and later built using the online tool dbdiagram.io. The schema is as follows:
<a  href="/documentation/db_schema_DevAssist.png"  target="_blank"><img  src="/documentation/db_schema_DevAssist.png"  alt="DevAssist DBj Schema"/></a>

The **users** table stores the **username** and **email address** of the registered user, both of which are unique. The **user** table has the **username** as a foreign key in the **posts**, **orders**, and **comments** tables.

The **posts** table has an **author** field which accepts the **username** from the **user** table, so each post has an unique user, It also has its **title** field as a foreign key in the **comments** table, link the post title and comment title together.

The **comments** table is linked to the **posts** and **users** table via the **username** as a foreign key, it is also link to the **posts** table via the **title** and **query** field, fully linking all comments to a specific logged in user.

The **donations** table stores the **name** and **description** of the 3 donations types currently available. It  has each donation name as a foreign key in the **order_line_items** table set as a foreign key thus linking the donation type to the order system at payment.

The **orders** table has the **order_line_item** as an inline table linked by their shared id. The orders table contains the details of the payment for each donation made and includes the **user** field as a foreign key from the **user** table containing the username. 
  

# Technologies Used

  

This project utilizes Python, Django, Postgres, SQLite, HTML, CSS and JavaScript technologies.

  

-  [Python](https://www.python.org/)
The project uses **Python 3** to develop the app, as part of the Django framework.

- [JQuery](https://jquery.com)
 The project uses **JQuery** as part of bootstrap 4 and to create a character counter on the text area fields.

-  [Bootstrap 4](https://getbootstrap.com/)
The project uses **Bootstrap** to simplify the structure of the website and make the website responsive easily.

-  **HTML 5 and CSS3**
The project uses **HTML5 and CSS3** for website structure and design.

-  [Google Fonts](https://fonts.google.com/)
I used the Ubuntu font from google as i thought in most suited for reading the post as its easy and clear on the eye. https://fonts.google.com/specimen/Ubuntu

-  [Django](https://www.djangoproject.com/)
The project uses the  **Django** framework to built the site. Django is a powerful high level web framework

-  [SQLite](https://www.sqlite.org)
The project uses **SQLite** relational database as its development level mysql database to store product, post and user information, it comes as part of the Django framework.

-  [Postgres](https://www.postgresql.org/)
The project uses **Postgres** relational database as its production level mysql database to store product, post and user information.

-  [GitHub](https://github.com/)
This project uses **GitHub** to remotely store the source code in a repository. The project can be cloned or downloaded from here. See [Deployment](#deployment) section

-  [StackEdit](https://stackedit.io)
This project uses **StackEdit** to build the markdown for this readme file

-  [Stripe](https://www.stripe.com)
This project uses **Stripe** to process credit card payments for user donations.

 
  
  

# Testing

  

I worked in sprints so every task was manually tested thoroughly via flash() messages or expected behaviors. I used my own kanban board with a small whiteboard and Post Its to track tasks. After each task completion, I would fully test it before moving on to the next task.

I also used the built in unit testing functionality of Django framework, these tests will only run on the development built in DB SQLite. They are run in the local environment via the ***python manage.py test*** command. All tests can be found in the **tests.py** file of the relevant app. It was my first time using unittesing so i covered all the main tests however there were some testing that i relied on the manual testing process.

The unit test summary is as follows:

| App| Tests Details| file location| 
| :------------- |:-------------| :-------------| 
| Account | testing load of login, register and logout pages | account/tests.py|
| Account | testing load of login, register and logout templates |  account/tests.py|
| Account | testing successful user login | account/tests.py|
| Account | testing successful submit of Register form | account/tests.py|
| Cart | testing redirect of url /cart/ to login when user not logged in| cart/tests.py|
| Cart | testing load of cart view page when user is logged in| cart/tests.py|
| Cart | testing load of cart view templates when user is logged in| cart/tests.py|
| Checkout | testing redirect of url /checkout/ to login when user not logged in| checkout/tests.py|
| Checkout | testing load of checkout view page when user is logged in| checkout/tests.py|
| Checkout | testing load of checkout view templates when user is logged in| checkout/tests.py|
| Donation| testing load of donation page /donate/| donation/tests.py|
| Donation| testing load of donation page template| donation/tests.py|
| Forum| testing load of forum landing page /community/ | forum/tests.py|
| Forum| testing load of forum landing page templates | forum/tests.py|
| Forum| testing redirect of forum add new post page (/community/query/new/)  when not logged in | forum/tests.py|
| Forum| testing load of forum add new post page (/community/query/new/)  when logged in | forum/tests.py|
| Forum| testing loading of the post detail page (/community/query/1/)   | forum/tests.py|
| Forum| testing loading of all the post detail page templates  | forum/tests.py|
| Forum| testing add post page (/community/query/new/) form accepts valid data and submits correctly   | forum/tests.py|
| Forum| testing add post page (/community/query/new/) form shows correct error message if required fields are filled in   | forum/tests.py|
| Forum| testing add comment form on post detail page accepts valid data and submits correctly   | forum/tests.py|
| Forum| testing edit post page (/community/query/1/edit) form loads all templates correctly  | forum/tests.py|
| Forum| testing edit post page form (/community/query/1/edit) submits correctly  | forum/tests.py|
| Main| testing load of the homepage /  | main/tests.py|
| Main| testing load of the about page /about  | main/tests.py|



## Manual testing

When the project was fully completed i went through the below manual testing scenarios to further test the project.

  

| Test | Expected |Passed |
| :------------- |:-------------| :-----:|
| User loads the landing page of site | Page displays without error when logged in or out, all page content is displayed correctly and navigation menu is functioning responsively | &#9745; |
| User loads the landing page of site whilst logged in | User only see links relevant to their logged in state and all links work as expected | &#9745; |
| User loads the about (/about/) page of site | Page displays without error when logged in or out | &#9745; |
| User loads the donations page of site | Page displays without error when logged in or out, all page content (3 donation products) is displayed correctly and navigation menu is functioning responsively | &#9745; |
| User clicks on add donation on donations page (/donate) when not logged in| User is redirected to log in before donation can be added to cart | &#9745; |
| User clicks on add donation on donations page (/donate) when logged in| Donation item is correctly added to users cart when cart is viewed (and is indicated on the top nav)| &#9745; |
| User loads community page (/community/) | Page displays without error when logged in or out, all page content is displayed correctly including any posts currently in the db and pagination links showing if necessary, navigation menu is functioning responsively| &#9745; |
| User clicks on Post title on the community page to load post details (/community/query/1) | Post Page displays without error when logged in or out, all page content is displayed correctly including any comments associated with the post currently in the db, navigation menu is functioning responsively| &#9745; |
| User clicks on Community help button on the community page to load the add post form (/community/query/new) when logged in | Add Post Page displays without error when logged in all page content and form is displayed correctly, navigation menu is functioning responsively| &#9745; |
| User clicks on Community help button on the community page to load the add post form (/community/query/new) when not logged in | User is redirected to login page | &#9745; |
| User clicks on Post title on the community page to load post details (/community/query/1) when logged in | Post detail Page displays without error as per normal and the option to edit/ delete post and add a comment appear| &#9745; |
| User clicks on delete or edit button on a Post that is not theirs | User is messaged that they do not own the post and the edit or delete action does not take place| &#9745; |
| User clicks on delete button on a Post that they own | Modal is loading warning user they are about to delete a post with the option to cancel or go ahead with the deletion| &#9745; |
| User  selects delete Post option on deletion modal | Post is deleted from db| &#9745; |
| User clicks on edit button on a Post that they own | Form is loaded with the details of the Post that are editable| &#9745; |
| User updates edit form with valid data | Form is submitted and new changes to the Post are display when the relevant Post detail page is loaded| &#9745; |
| Logged in user clicks on add comment option in Post detail page| Add comment form loads| &#9745; |
| User adds valid data to the add comment form | Add comment form submits and comment displays on the post detail page| &#9745; |
| User selects login option | Log in Page displays without error , all page content and form is displayed correctly and navigation menu is functioning responsively| &#9745; |
| User enters invalid data in login form  | User is messaged and not logged in| &#9745; |
| User enters valid data in login form  | User is messaged and logged in successfully| &#9745; |
| User selects Register option | Register Page displays without error , all page content and form is displayed correctly and navigation menu is functioning responsively| &#9745; |
| User enters invalid data in Register form  | User is messaged and registration not submitted| &#9745; |
| User enters an existing username or email address in Register form  | User is messaged and registration not submitted| &#9745; |
| User enters valid data in Registration form  | User is messaged and log in page loads| &#9745; |
| User loads cart page with items in cart and selects the checkout option  | Checkout Page displays without error, all page content, items to be ordered, total cost and payment form are displayed correctly and navigation menu is functioning responsively| &#9745; |
| User enters invalid data in Payment form  | User is messaged as appropriate to incorrect data or card detail and payment does not go through| &#9745; |
| User enters valid data in Payment form  and uses the test Stripe credit card details | User is messaged and payment goes through successfully and appears in the Stripe test dashboard| &#9745; |
| User selects the logout option  | user is successfully logged out and messaged| &#9745; |
| User selects password reset option from login form page  | Reset password Page displays without error , all page content and form is displayed correctly and navigation menu is functioning responsively| &#9745; |
| User enters  and existing registered email address in password reset form  | Reset email is to email address entered by the user| &#9745; |
| User enters email address not in already registered  | Reset email is not sent| &#9745; |
| User clicks through on password reset email link | Password reset page loads with the relevant form to enter new password details | &#9745; |
| User enters valid date on password reset form| Password is reset and user can now log in with new password details | &#9745; 
| User loads the about (/about) page of site | About page displays without error when logged in or out, all page content is displayed correctly and navigation menu is functioning responsively | &#9745; |
| User is currently logged in | User will see different top and bottom navigation items relevant to their current logged in state | &#9745; |
| User is currently not logged in | User will see different top and bottom navigation items relevant to their current logged  out state | &#9745; |
| User enters a page url that does not exist on the site| 404 page displays without error when logged in or out, all page content is displayed correctly and navigation menu is functioning responsively | &#9745; |




# Coding Notes

The site uses python 3,7 and the Django 2.2 framework.

Some of the features of the code are as follows:

The main and about pages load via the ***dev_assist/main/urls.py/***  file redirected from the ***dev_assist/dev_assist/urls.py/*** file:
~~~
dev_assist/dev_assist/urls.py/:

path('', include('main.urls')),

..................

dev_assist/main/urls.py/:

path('', views.home, name='home'),
path('about/', views.about, name='about'),
~~~
This method of setting the urls is also used in the cart, checkout and forum apps:
~~~
dev_assist/dev_assist/urls.py/:

path('community/', include('forum.urls')),
path('cart/', include('cart.urls')),
path('donate/', donation_view.donations, name='donations'),
path('checkout/', include('checkout.urls')),
~~~

### User authentication feature

I use the built in django auth methods to create new users and log them in or out. The urls for these are also set in the dev_assist app in urls.py

~~~
dev_assist/dev_assist/urls.py/:

from account import views as user_views

path('register/', user_views.register, name='register'),
# using the built in log in view to allow log user in
path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
# using the built in log out functionality
path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
~~~
the import statement pulls in the ***account/views.py*** file which then tells django which function in the account/views.py file to look at eg ***path('register/', user_views.register, name='register')*** is telling django to look at the function called register in the ***account/views.py*** file for further processing of the **/register** url, the name value is used to define the url when linking to the page eg. ***href="{% url 'register' %}"***.
The register form is located in the ***account/forms.py*** file which defines the that Im using the built in User model and the built in  ***UserCreationForm***.
~~~
from django.contrib.auth.models import User # built in
from django.contrib.auth.forms import UserCreationForm # from built in django
~~~
The ***UserRegistrationForm*** function creates the form with the built in ***User*** model and defines which fields to use in the form
~~~
class UserRegisterForm(UserCreationForm):
	email = forms.EmailField() # creating email field
	class Meta: # additional metadata for form
	model = User # using built in User model
	fields = ['username', 'email', 'password1', 'password2'] 
~~~
The ***clean_email*** function checks to db to ensure the the email address entered on the register form is unique. This was adapted from a stackoverflow article.

The ***register*** function in the ***account/views.py*** checks if the form has been submitted and then validates the data only adding the user to the db if it passes all validation checks.
~~~
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,f'Account created! You can now log in')
			return redirect('login')

	form = UserRegisterForm()
	context={
	'title':'Register',
	'form': form
	}
	return render(request, 'register.html', context)
~~~
In the ***settings.py*** file the django app is informed where to redirect to once there is a successful submit.
~~~
LOGIN_URL = 'login'
~~~

The remaining 2 paths for login and logout are using the built in django views  to process and will look to the relevant template name defined to  load in the html etc for that page.
~~~
path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login')
~~~

### Navigation text display for mobile

I felt that given the amount of items in the top nav that it looked a little cluttered with the names of the link alongside the nav icons so I set the nav link names to only show on smaller devices thus giving a cleaner look on the top nav for larger devices.
~~~
<a class="nav-item nav-link " href="{% url 'donations' %}" title="donate">
<i class="fa fa-thumbs-o-up fa-2x fa-fw" aria-hidden="true"></i>
<!-- only showing nav names on mobiles and tabs, hiding for larger devices for better viewing-->
<div class="d-inline d-none d-sm-block d-lg-none"> Donations</div></a>
~~~

### Cart and Checkout
The cart is accessible from all pages once logged in. This is done using a function set in the **cart/contexts.py** file. The cart will have items added from the the donations page /donate/ and on the cart view page items can be removed, the check button is also displayed to progress the order from the cart to the checkout.
The app knows to use the contexts file as its set in the project **settings.py** file:
~~~
'context_processors': [
	'cart.contexts.cart_contents', # this is the context.py file in the cart app, This makes it available on every page
],
~~~
**contexts.py** file:
~~~
from django.shortcuts import get_object_or_404
from donation.models import Donation

def cart_contents(request):
	cart = request.session.get('cart', {})
	cart_items = []
	total = 0
	donation_count = 0
~~~
the above sets the cart to its 'empty' state. Then below, the cart (stored in the session) is looped through and displayed.
~~~
	for id, quantity in cart.items():
	donation = get_object_or_404(Donation, pk=id)
	total += quantity * donation.price
	donation_count += quantity
	cart_items.append({'id': id, 'quantity': quantity, 'donation': donation})
	return {'cart_items': cart_items, 'total': total, 'donation_count': donation_count}
~~~
Both the checkout and the cart functionalities are mostly based on what we learned for the course lessons. The checkout uses Stripe to verify the user card details. And saves the users order (donation)  to the db if payment is successful. The javascript for the Stripe functionality is as from course and is stored in static/js/stripe.js. I am using version 2 of stripe, the below snippet is called in the checkouts template (**/checkout/templates/checkout/checkout.html**) and is standard use.
~~~
<script type="text/javascript" src="https://js.stripe.com/v2/"></script>
<script type="text/javascript">
//<![CDATA[
Stripe.publishableKey = '{{ publishable }}';
//]]>
</script>
<script type="text/javascript" src="{% static 'js/stripe.js' %}"></script>
~~~
The order form (**/checkout/forms.py**) uses the model as set in (**/checkout/models.py**). Each donation item is also set as an inline item in the orders model class so that when an order is submitted so too is the donation items purchased and these are saved to the relevant db.
~~~
class Order(models.Model):
	full_name = models.CharField(max_length=50, blank=False)
	phone_number = models.CharField(max_length=20, blank=False)
	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	date = models.DateField()
~~~
~~~
class OrderLineItem(models.Model):
	order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
	donation = models.ForeignKey(Donation, null=False, on_delete=models.CASCADE )
	quantity = models.IntegerField(blank=False)
~~~
Both the payment and order forms are called and displayed in the **checkout/templates/checkout/checkout.html** template. The payment form is required by Stripe.

~~~
class MakePaymentForm(forms.Form):
MONTH_CHOICES = [(i, i) for i in range(1, 12)]
YEAR_CHOICES = [(i, i) for i in range(2019, 2036)]
credit_card_number = forms.CharField(label='Credit card number', required=False)
cvv = forms.CharField(label='Security code (CVV)', required=False)
expiry_month = forms.ChoiceField(label='Expiry Month', choices=MONTH_CHOICES, required=False)
expiry_year = forms.ChoiceField(label='Expiry Year', choices=YEAR_CHOICES, required=False)
stripe_id = forms.CharField(widget=forms.HiddenInput)

class OrderForm(forms.ModelForm):
class Meta:
model = Order
fields = (
'full_name', 'phone_number'
)
~~~
The checkout function in the **checkout/views.py** file then processes the actions on the page:

Secret stripe key is set at the top of the file
~~~
stripe.api_key = settings.STRIPE_SECRET
~~~
login decorator is used to check if the user is logged in before displaying checkou
~~~
# user must be logged in to see checkout
@login_required
def checkout(request):
~~~
Checking cart contents and if nothing is in cart the user is sent to the donations page
~~~
cartcontent = request.session.get('cart', {})
if not cartcontent:
	messages.warning(request,f'Your Cart has no donations!! ')
	return redirect(reverse('donations'))
~~~
if the forms are submit the are checked and if valid the form details are saved, cart is looped through and order is successful order is save to db
~~~
user = request.user
if request.method == "POST":
	order_form = OrderForm(request.POST)
	payment_form = MakePaymentForm(request.POST)
	if order_form.is_valid() and payment_form.is_valid():
	order = order_form.save(commit=False)
	order.date = timezone.now()
	order.user = user
	order.save()

~~~
~~~
for id, quantity in cart.items():
donation = get_object_or_404(Donation, pk=id)
total += quantity * donation.price
# adding order to db
order_line_item = OrderLineItem(
order=order,
donation=donation,
quantity=quantity)
order_line_item.save()
~~~
Stripe is queried and relevant messages are returned to the user, payment is processed if valid card (Stripe test card details) is entered.
~~~
try:
# processing stripe payment
customer = stripe.Charge.create(
amount=int(total * 100),
currency="EUR",
description=request.user.email,
card=payment_form.cleaned_data['stripe_id'],)
~~~
display card errors
~~~
# display card errors if any
except stripe.error.CardError:
messages.error(request, "Your card was declined!")
~~~
Process successful order and message user, clear cart and load donations page
~~~
# if payment is successful empty cart content and inform user
if customer.paid:
messages.success(request, f'You have successfully paid')
request.session['cart'] = {}
return redirect(reverse('donations'))
~~~
message any other errors
~~~
else:
messages.error(request, "Unable to take payment")
else:
print(payment_form.errors)
messages.error(request,"We were unable to take a payment with that card!")

~~~
The below will load page forms on page load
~~~
else:

# loading payment forms
payment_form = MakePaymentForm()
order_form = OrderForm()
eturn render(request, "checkout/checkout.html",
{'order_form': order_form, 'payment_form': payment_form,'publishable': settings.STRIPE_PUBLISHABLE})
~~~
### Forum
The forum landing page (/community) checks for posts in the db and uses the built in django pagination to display the posts
~~~
from django.core.paginator import Paginator
~~~
~~~
def community(request):
	querys = Post.objects.all()
~~~
All available posts, the posts are then paginated to show 3 posts per page, with the default page number set to 1. The current page is passed to the template and loaded
~~~
	page = request.GET.get('page', 1)
	paginator = Paginator(querys, 3)
	post_pag = paginator.get_page(page)
	context = {
	"posts": post_pag
	}
	return render(request,"forum/forum_list.html", context)

~~~
The next and previous buttons for the pagination exist in the template
**forum/templates/forum/forum_list.html:**
~~~
{% if posts.has_other_pages %}
<ul class="pagination">
~~~
checking to see if there are posts previous to the current displayed ones and if so showing the previous links to the previous page(s)
~~~
{% if posts.has_previous %}
<li class="page-item"><a class="page-link" href="?page={{ posts.previous_page_number }}">&laquo;</a></li>
{% else %}
~~~
if there are no previous posts the previous link is hidden
~~~
<li class="disabled page-item"><span class="page-link">&laquo;</span></li>
{% endif %}
~~~
looping through posts for the current page and displaying
~~~
{% for i in posts.paginator.page_range %}
<!-- showing current active page -->
{% if posts.number == i %}
<li class="active page-item"><span class="page-link">{{ i }} <span class="sr-only">(current)</span></span></li>
{% else %}
<li><a class="page-link" href="?page={{ i }}">{{ i }}</a></li>
{% endif %}
{% endfor %}
~~~
if there are more pages show the next link or hide it if there are no more pages
~~~
{% if posts.has_next %}
<li class="page-item"><a class="page-link" href="?page={{ posts.next_page_number }}">&raquo;</a></li>
{% else %}
<!-- disable next link if there are no more pages-->
<li class="disabled page-item"><span class="page-link">&raquo;</span></li>
~~~
The add post form at **forum/forms.py** is used to add a post to the db and is based on the model at **forum/models.py**  The model has a 'title' , 'author', 'content' and 'date_posted' field set in the order of date posted. The form, once valid, is posted to the db upon successful submit. The user needs to be logged in to add a post. This is done in the 'create_query' function and uses the login required decorator

**forum/views.py:**
~~~
from django.contrib.auth.decorators import login_required
~~~
~~~
@login_required
def create_query(request):
~~~
The edit_query function also uses the same form and model to edit an existing post. 

The post detail page shows all detail of the post and will also show edit and delete post  and add comment options if the user is logged in. The add comment form is also found in the same file as the add post and works in a similar manner.

### forum search
The search function also lives in the forum app in **views.py**.  The search will search the content and title fields of all Posts in the db. To allow multiple field searches i used the Q functionality in django:
~~~
from django.db.models import Q # for multiple searchs
~~~
the values passed from the search form on the top navigation are passed to the 'query' variable.
~~~
def do_search(request):
	query = request.GET.get('q')
~~~
I then use the Q functionality to check the relevant db table fields for the query entered by the user. If there are no posts with the user query the user is messaged. Any posts the qualify the query search are then returned to the template and displayed.
~~~
	posts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
	if not posts:
		messages.warning(request,
		f'Your serach for "{query} " returned no results')
	context = {
	"posts": posts
	}
	return render(request, "forum/forum_list.html", context)
~~~
## Deployment

I personally used vscode on my local machine to develop the site using Python 3.7.3  and deployed to Heroku via Github.

1. To download or clone the site to your local machine you will need to go to my [repo](https://github.com/alimgee/book-review-milestone-project3) see steps in https://help.github.com/en/articles/cloning-a-repository .
2.  Before you download or clone the site you will need to ensure you have [Python 3.7](https://www.python.org/downloads/) installed. 
3. Once you have Python installed, create a virtual environment as appropriate to you chosen IDE and os.
4. Install all requirements via the requirements.txt file using the *****pip _install_ -r _requirements_.txt***** command once you have activated your virtual environment.
5. Use the command ***python manage,py runserver*** to get the project running on your localhost.
6. You will need to change the email settings in **settings.py** to get the project  to send password reset emails via your own email services.
7. I used Heroku to host the public version of my app. I used a postgres add on for my db on the Heroku app and set all secret environmental values in the config vars in the settings of the heroku app. I linked the Heroku app to the github repo via the deployment section of the Heroku app and done a manual deploy from there. I used gunicorn to run the app in heroku and whitenoise to manage the static files. A procfile is also needed by heroku with the line ***web: gunicorn dev_assist.wsgi:application*** to let heroku know how to run the web app. Heroku also requires the **requirement.txt** file to inform it of any relative dependencies for the app.


### Acknowledgements

This is the last project  in the Fullstack Frameworks Dev course and so brings an end to the beginning of my dream of becoming a developer, I am so proud to have got this far and completed the course and look forward to where my learnings now bring me. 

Special thanks to the below:

**Code Institute** tutors for their assistance in getting me this far in the course.

**Code Institute** course material and learnings which were relied on for this development

All the folk in the <strong>Code Institute Slack </strong> for their invaluable input to their fellow members development, in particular **JoWings** who spent a hour of her time on a sunday afternoon trying to help me with an issue with my foreign keys. I also learned a lot for this project from the [Corey Schaffer](https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g) series of you tube videos on python and Django.

Also to various Stackoverflow articles for the pointers that often set me in the right direction to resolving issues. with my code.




#### Disclaimer

The content of this website is educational purposes only and should not be used on a real world basis.
