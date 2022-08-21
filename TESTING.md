# Testing 

During my development for this project each function were tested to work as expected. Each section in this file describes all of the different tests. 

**Remember that all links in this Testing file does not open in a new tab. They open in the same window.**


---
## Table of contents - testing

* [Validation Testing](#validation-testing)
  * [Python PEP8](#python-pep8-validation)
  * [HTML Validation](#html-code-validation)
  * [CSS Validation](#css-code-validation)

* [User Story Testing](#user-story-testing)

* [Device Testing](#device-testing)

* [Manual Testing](#manual-testing)
  * [Standard Elements](#standard-elements)
  * [Home Page](#home-page)
  * [Recipe Details](#recipe-details)
  * [Add Recipe](#add-recipe)
  * [Authentication](#authentication)

* [Defensive Programming](#defensive-programming)


---
## Validation Testing

### Python (PEP8) Validation 

I have tested my python code at [PEP8 online validation tool](http://pep8online.com/), I will show my results below with images and then a short description below each image of my solution. And I have seperated each django file to their respective django application within the project, the main application whattoeat and the recipes app. 

##### whattoeat Main Project App 

**settings.py:**

**urls.py:**

##### recipes App 

**forms.py:**

**models.py:**

**urls.py:**

**views.py:**

### HTML Code Validation 

When testing my markup HTML code at [W3C HTML Validator](https://validator.w3.org/), I got one error: 

**Error:** 

I had missed to erase a `"closing i element (</i>)"`, for my `What To Eat` logo at the top of the website.

**Solution:**

The reason for why I had a closing `(</i>)` tag is because I first wanted to have a `Font Awesome` icon before my logo text, but I decided not to and then forgot it there. 
So my solution for this error was to just erase this missing closing tag. 

**After I applied the HTML solution:**

Now you can take a look at my `approved` HTML validation by clicking this link [here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwhattoeat2022.herokuapp.com%2F).

### CSS Code Validation

---
## User Story Testing

Here is my user story testing for this project as a **guest**:

1. As a **guest** I would like to be able to register an account using a username, email and password. 

- I have installed `allauth` to handle all of my authentication, and then I have been styling each file for `Login, Logout, Sign up` so a every guest can `Sign up` for an account or users can `Login/Logout`. 

1. As a **guest** I would like to be able to learn more about the website. 

- I added a link in my navigation bar `About` that triggers a **modal** that appears on the screen with information about the website. 

1. As a **guest** I would like to be able to visit the website's social media links. 

- I added the social media links in the `footer`, each link opens in a seperate tab. 

1. As a **guest** I would like to be able to view all of the recipes. 

- I created a list of all the recipes, they are soreted in a order of six recipes on each page and this is done with site pagination. The guest or the user can navigate to each page with the `next and previous` buttons underneath the recipe list. 

1. As a **guest** I would like to be able to view the recipe details of a selected recipe. 

- I've made sure that when a guest or user clicks on `View recipe` for a selected recipe a sperate page with all the recipe details will appear. 
Including `Title, created on, author, recipe image, difficulty, serves, prep time, cook time, ingredients, instructions`. 

Here is my user story testing for this project as a **user**:

1. As a **user** I would like to be able to login to my account. 

- I have made sure by using `allauth` that a user can login to their account. 

1. As a **user** I would like to be able to add recipes to the list of recipes. 

- I have made sure that a authenticated user can add recipes to the list of recipes. 

1. As a **user** I would like to be able to edit and delete recipes created by me. 

- I ahve made sure that only the `author` of the recipe can `edit or delete` the specific recipe. 

Here is my user story testing for this project as a **admin**:

1. As a **admin** I need to be able to see the entire list of recipes that has been added. 

- In the admin panel the admin can see all of the recipes that has been created. 

1. As a **admin** I need to be able to add recipes to the list of recipes to be viewed by everyone. 

- In the admin panel the admin can add recipes to the list of recipes. 

1. As a **admin** I need to be able to edit and delete recipes created by me. 

- As an admin you can edit and delete recipes in the admin panel. 


---
## Device Testing

Something that's worth mentioning is that I've tested the majority of these devices within Chrome dev tool, I have not had physical access to test these devices. I have tested the responsiveness and aesthetics on the following devices and browsers:

* Apple 

* Android

* Google Devices

* Motorola

* Desktops/laptops

* Browsers


---
## Manual Testing

### Standard Elements

I was testing so my most common elements of my website was working correct, such as: 

* Make sure so my Logo of `What To Eat` always direct the user back to the home page. 
* Test so my navigation links work as expected. 
* Test so my social media links in the `footer` works correctly and opens in a new tab. 

### Home Page 

I was manualy testing my home page for these elements: 

* When a user login a green message on the top of the home page appears so the user knows that the login was successful. This message also appears when the user logout. 
* Make sure so the `View recipe` button on each recipe card directs the user to that specific recipe details. 

### Recipe Details

I was manualy testing so these functions and elements was working correct: 

* Make sure so `only` the author of each recipe can see the green `Edit recipe` and red `Delete recipe` buttons by checking the authentication of each user that want to see recipe details. 
* Make sure so `only` the author can edit the recipe. 
* Make sure so `only` the author can delete the recipe. 
* Make sure that my `delete modal` is appearing when the author of the specific recipe choose to delete it. 

### Add Recipe

I was manualy testing so the elements of this page was working correct: 

* Make sure so the recipe `slug` was unique for each recipe like a `ID`. 
* Make sure so the user gets a warning message is the user tries to add a recipe with the same title as another recipe. 
* Make sure so a user can't add unrealistic numbers for the cooking process like, for how many `Serves` this message will appear `Ensure this value is less than or equal to 14.`, 
for how long `Prep time` this message will appear `Ensure this value is less than or equal to 100.` and for 
`Cook time` this message will appear `Ensure this value is less than or equal to 300.`. 
* Make sure that add recipe and edit recipe get saved to the list of recipes. 

### Authentication

I was manualy testing so the authentication for each page worked correct: 

* Make sure so the `Login` page only accepts the correct username and password, and then directs the user back to the home page. 
* Make sure so the `Logout` page appears with `You are about to sign out. Is that what you want?` message and then directs the user back to the home page. 
* Make sure so the `Sign up` page works correctly and directs the user back to the home page. 


---
## Defensive Programming

After my second session with my mentor [Benjamin Kavanagh](https://github.com/BAK2K3) I got the feedback that I should implement `Defensive Programming` for my `CRUD functionality` which stands for `Create, Read, Update, Delete` and that is translated to my `Add recipe for "Create", Edit recipe for "Update", Delete recipe for "Delete"`. The `Read functionality` is just the way a guest or user can view a recipe, but that isn't a part of `Defensive Programming` since you doesn't need to be authenticated to view the recipes. 

So on to what I did to improve my backend code the way I did in the front end code is that I added a `@login_required` decorator that is a part of `Django decorators` (read more about django decorators [here](https://docs.djangoproject.com/en/dev/topics/auth/default/#the-login-required-decorator)), to ensure that what ever guest or user that is trying to access either `Add recipe, Edit recipe or Delete recipe` is authenticated. 

For my `Edit recipe and Delete recipe` I wanted to make sure that only the `author` (creator of that recipe) could `Edit or Delete` the specific recipe, otherwise the guest or user would be directed to my custom `403 error page`.

Here are some screenshots of my function based views in views.py: 

**Add recipe:**

![Screenshot of function based views in views.py, add_recipe](/assets/readme/testing-readme/add_recipe.png)

**Edit recipe:**

![Screenshot of function based views in views.py, add_recipe](/assets/readme/testing-readme/edit_recipe.png)

**Delete recipe:**

![Screenshot of function based views in views.py, add_recipe](/assets/readme/testing-readme/delete_recipe.png)


---
## RETURN BACK TO TOP [here](#testing)