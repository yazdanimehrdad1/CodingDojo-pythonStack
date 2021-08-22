##################################################################################################
#How to reorder the list and pass it to the django template (filter)
##################################################################################################
#https://docs.djangoproject.com/en/dev/topics/db/queries/#retrieving-specific-objects-with-filters
def wall(request):
    users = User.objects.all()
    messages= Message.objects.all().order_by('created_at').reverse()
    
    context={
        "users":users,
        "messages":messages

    }
    return render(request, 'main.html',context)


##################################################################################################
#For the one to many relationships, try to create it on the many side
##################################################################################################
# in the snippet below, each user has many messages:

def create_message(request):
    Message.objects.create(
        message= request.POST['message'],      # this comes from the html template
        message_created_by = User.objects.get(id= request.session["user_id"]) # this either comes from session or the user_id shaould be passed as an argument</div>
    )

    return redirect('/wall')


##################################################################################################
#Validation
##################################################################################################



class ShowManager(models.Manager):
    def validate(self, form):
        errors = {}
        if len(form['title']) < 2:
            errors['title'] = 'Title field should be at least 2 characters'
        if len(form['network']) < 3:
            errors['network'] = 'Network field should be at least 3 characters'
        if form['description'] != '' and len(form['description']) < 10:
            errors['description'] = 'Description should be at least 10 characters'
        if datetime.strptime(form['release_date'], '%Y-%m-%d') > datetime.now():
            errors['release_date'] = 'Release Date should be in the past'
        return errors

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateTimeField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

######


from django.db import models
import re
import bcrypt


class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        # Length of the first name
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least two characters long"

        # Length of the last name
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least two characters long"

        # Email matches format
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['email']) == 0:
            errors['email'] = "You must enter an email"
        elif not email_regex.match(postData['email']):
            errors['email'] = "Must be a valid email"

        # Email is unique
        current_users = User.objects.filter(email=postData['email'])
        if len(current_users) > 0:
            errors['duplicate'] = "That email is already in use"

        # Password was entered (less than 8)
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characers long"
        if postData['password'] != postData['confirm_password']:
            errors['mismatch'] = "Your passwords do not match"

        # age verification
        user_birthday  = datetime.strptime(postData['birthday'], '%Y-%m-%d')     
        age = (datetime.now() - user_birthday).days/365 
        print("User age", age)
        if age<18:
            errors['birthday'] = "must be older than 18 years old"

        return errors

    def login_validator(self, postData):
        errors = {}
        existing_user = User.objects.filter(email=postData['email'])
        if len(existing_user) != 1:
            errors['email'] = "User does not exist."
        # email has been entered
        if len(postData['email']) == 0:
            errors['email'] = "Email must be entered"
        # Password has been entered
        if len(postData['password']) < 8:
            errors['password'] = "An eight character password must be entered"
        # if the email and password match
        elif bcrypt.checkpw(postData['password'].encode(), existing_user[0].password.encode()) != True:
            errors['mismatch'] = "Email and password do not match"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    


# in the views.py
def login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        this_user = User.objects.filter(email=request.POST['email'])
        request.session['user_id'] = this_user[0].id
        return redirect('/success')
    return redirect('/')




def show_all(request):
    # check to see if the user loggedin or registered by checking their session <p></p>
    if "user_id" not in request.session:
        return redirect('/')
    else:
        context = {
            'all_books': Book.objects.all(),
            'this_user': User.objects.get(id=request.session['user_id'])
        }
        return render(request, 'books/show_all.html', context)



def create_book(request):
    errors = Book.objects.book_validator(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books')
    else:
        user = User.objects.get(id=request.session["user_id"])
        book = Book.objects.create(
            title = request.POST['title'],
            description = request.POST['description'],
            creator = user
        )
        # bonus: the book creator automatically favorites the book
        user.favorited_books.add(book) # Here we have a many to many relationship</p>

        return redirect(f'/books/{book.id}')



def create_book(request):

    errors = Book.objects.validator_book(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books')
    user =User.objects.get(id = request.session['user_id'])
    new_book = Book.objects.create(
        title = request.POST['title'],
        description = request.POST['description'],
        creator = user
    )
    #Both of this would work<p> Favorit books is a good projects for many to many practices</p>
    # user.favorited_books.add(new_book)
    new_book.favorited_by.add(user)

    return redirect(f'/books/{new_book.id}')


# Dojo_ninjas project  -- 
def add_ninja(request):
    if request.method=="GET":
        return redirect('/')
    
    ninja = Ninja.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        # Either one of the following scrips would work. The second one is using 
        # the exsiting models.objects property to reach the id 
        # you can see that in the models.py for the Ninja class we don't have
        # the dojo_id instead we have the dojo itself. 
        
        # dojo = Dojo.objects.get(id= request.POST['dojo'])
        dojo_id = request.POST['dojo']
    )
    return redirect('/')