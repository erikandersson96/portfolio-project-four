# Testing 

During my development for this project each function were tested to work as expected. Each section in this file describes all of the different tests. 

### HINT:
**Remember that all links in this Testing file does not open in a new tab. They open in the same window (I have marked them with "(link)").**


---
## Table of contents - testing

* [Validation Testing](#validation-testing)
  * [Python PEP8](#python-pep8-validation)
  * [HTML Validation](#html-code-validation)
  * [CSS Validation](#css-code-validation)
  * [Lighthouse](#lighthouse)
  * [WAVE](#wave)

* [User Story Testing](#user-story-testing)

* [Device Testing](#device-testing)

* [Manual Testing](#manual-testing)
  * [Standard Elements](#standard-elements)
  * [Home Page](#home-page)
  * [Recipe Details](#recipe-details)
  * [Add Recipe](#add-recipe)
  * [Authentication](#authentication)
  * [About Modal](#about-modal)
  * [My favorites](#my-favorites)

* [Defensive Programming](#defensive-programming)

* [Automated Tests](#automated-tests)


---
## Validation Testing

### Python (PEP8) Validation 

I have tested my python code at [PEP8 online validation tool](http://pep8online.com/) (link), I will show my results below with images and then a short description below each image of my solution. And I have seperated each django file to their respective django application within the project, the main application whattoeat and the recipes app. 

#### whattoeat Main Project App 

**settings.py:**

![Screenshot pep8 validation settings.py](/assets/readme/testing-readme/pep8-settings.png)

**Solution settings.py:**

I added a backslash to get rid of the line too long warning for line 162, and I made sure that I got the correct `python indentation` by pressing the tab key on my keyboard. 

**urls.py:**

![Screenshot pep8 validation whattoeat urls.py](/assets/readme/testing-readme/pep8-wte-urls.png)

I got no errors when I tested the `whattoeat` urls.py code. 

#### recipes App 

**admin.py:**

![Screenshot pep8 validation recipes admin.py](/assets/readme/testing-readme/pep8-recipes-admin.png)

**forms.py:**

![Screenshot pep8 validation recipes forms.py](/assets/readme/testing-readme/pep8-recipes-forms.png)

**Solution forms.py:**

Since I got a warning of `blank line contains whitespace` I erased it by doing a backspace on my keyboard an then save the file.

**models.py:**

![Screenshot pep8 validation recipes models.py](/assets/readme/testing-readme/pep8-recipes-models.png)

**Solution models.py:**

I got two warnings for my `recipe models.py file`, one for not using two blank lines and a blank line contains whitespace so I solved these by adding two blank lines and erase the whitespace. 

**urls.py:**

![Screenshot pep8 validation recipes urls.py](/assets/readme/testing-readme/pep8-recipes-urls.png)

**Solution urls.py:**

I got a warning for `line too long`, so I fixed this by breaking up the line into two and use the right indentation. 

**views.py:**

![Screenshot pep8 validation recipes views.py](/assets/readme/testing-readme/pep8-recipes-views.png)

**Solution views.py:**

I fixed the two warnings of `line too long` by erasing commented out code that was too long and unnecessary and splitting up the warning for line 56 into two lines of code with the correct
indentation.

#### profiles App

**admin.py:**

![Screenshot pep8 validation profiles admin.py](/assets/readme/testing-readme/pep8-profiles-admin.png)

**models.py:**

![Screenshot pep8 validation profiles models.py](/assets/readme/testing-readme/pep8-profiles-models.png)

**urls.py:**

![Screenshot pep8 validation profiles urls.py](/assets/readme/testing-readme/pep8-profiles-urls.png)

**views.py:**

![Screenshot pep8 validation profiles views.py](/assets/readme/testing-readme/pep8-profiles-views.png)


### HTML Code Validation 

When testing my markup HTML code at [W3C HTML Validator](https://validator.w3.org/) (link), I got one error: 

**Error:** 

I had missed to erase a `"closing i element (</i>)"`, for my `What To Eat` logo at the top of the website.

**Solution:**

The reason for why I had a closing `(</i>)` tag is because I first wanted to have a `Font Awesome` icon before my logo text, but I decided not to and then forgot it there. 
So my solution for this error was to just erase this missing closing tag. 

**After I applied the HTML solution:**

Now you can take a look at my `approved` HTML validation by clicking this link [here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwhattoeat2022.herokuapp.com%2F) (link).


### CSS Code Validation

When I first tested my CSS code via [W3C Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/validator.html.en) (link), by enter my heroku website link like I have done this previously with my other projects (but then I used the github link). But then I got 6 errors for Font Awesome like shown in the image below. So I asked my mentor [Benjamin Kavanagh](https://github.com/BAK2K3) (link) why this was the case because it seemed to be a problem not related to my CSS but rather something regarding my CDN link for Font Awesome, so I was told to not test my CSS by typing in the website link but instead copy my CSS and paste it in the `By direct input` and test it that way and then I got it right with no errors. 

**First wrong attempt with errors:** 

![Screenshot of css wrong attempt](/assets/readme/testing-readme/css-validering-2.png)

**The correct attempt with no errors:**

Now you can take a look at my `approved` CSS validation by clicking this link [here](https://jigsaw.w3.org/css-validator/validator) (link).


### Lighthouse

I have tested the website with `Chrome lighthouse dev tool` to test the website `performance`. I have tested this in a `incognito` window for better performance while testing. I got an average result of 94,5% for desktop and 90,5% for mobile devices.

**Desktop:**

![Screenshot of lighthouse devtool on desktop](/assets/readme/wave-lighthouse/desktop-lighthouse.png)

**Mobile:**

![Screenshot of lighthouse devtool on mobile](/assets/readme/wave-lighthouse/mobile-lighthouse.png)


### Wave

`What To Eat` website has been tested at [WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/) (link). `WAVE` is a suite of evaluation tools that helps authors make their web content more accessible to individuals with disabilities (Taken from Wave website). And I got `7` contrast errors and `1` alert for `Suspicious alternative text` for the start page like demonstrated in the image below: 

**WAVE errors and alert:**

![Screenshot of contrast error and alerts](/assets/readme/wave-lighthouse/wave-wrong.png)

**Solution WAVE errors and alert:**

You can look at the approved result [here](https://wave.webaim.org/report#/https://whattoeat2022.herokuapp.com/) (link). 

I solved the `alert` by replacing the first alternative text of my background image to something more specific like `background image of ingredients to use in cooking`. 

I solved the `7 contrast errors` by using [Webaim online contrast checker](https://webaim.org/resources/contrastchecker/) (link) for help to find an accepted contrast ratio, the accepted ratio is `4.51:1` between `Foreground Color` and `Background Color`. 

When testing the other pages `Add recipe, Register, Login` I got `1 Alert` for missing `h1` (I have used a h3 heading instead), since I tought that a `h3` looked better I will stay with it and since this is just an `Alert and not an Error`. The `Add recipe, Edit recipe and My favorites` isn't tested because I have to be logged in to test those but `WAVE` won't let me login while testing or before testing. For the link at `Register` page, that says you can login if you already got an account got `1 Alert` for `Redundant link`, I will leave this as it is as well since this is just an `Alert and not an Error`. 

**Alert for missing h1:**

![Screenshot of alerts h1](/assets/readme/wave-lighthouse/h1-alert.png)

![Screenshot of alerts h1](/assets/readme/wave-lighthouse/h1-alert-2.png)

**Alert for Redundant link:**

![Screenshot of alert redundant link](/assets/readme/wave-lighthouse/register-alert.png)

![Screenshot of alert redundant link](/assets/readme/wave-lighthouse/register-alert-2.png)

![Screenshot of alert redundant link](/assets/readme/wave-lighthouse/register-alert-3.png)


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

- I have made sure that only the `author` of the recipe can `edit or delete` the specific recipe. 

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
  * iPhone 4
  * iPhone SE
  * iPhone XR
  * iPhone 12 Pro
  * iPhone 6/7/8
  * iPhone 6/7/8 Plus
  * iPad Mini

* Android
  * Samsung Galaxy S8+
  * Samsung Galaxy S20 Ultra

* Motorola
 * Moto G4

* Desktops/laptops/monitor
  * MacBook Pro 13"
  * Lenovo 24" monitor

* Browsers
  * Chrome 
  * Safari


---
## Manual Testing

### Standard Elements

I have manualy tested so my most common elements of my website is working correct, such as: 

* Make sure so my Logo of `What To Eat` always direct the user back to the home page. 
* Test so my navigation links work as expected. 
* Test so my social media links in the `footer` works correctly and opens in a new tab. 

### Home Page 

I have manualy tested my home page for these elements: 

* When a user login a green message on the top of the home page appears so the user knows that the login was successful. This message also appears when the user logout. 
* Make sure so the `View recipe` button on each recipe card directs the user to that specific recipe details. 
* Make sure so a user can't manually type in a page number that doesn't exists for the `page pagination` to trigger an error.

### Recipe Details

I have manualy tested so these functions and elements works correct: 

* Make sure so `only` the author of each recipe can see the green `Edit recipe` and red `Delete recipe` buttons by checking the authentication of each user that want to see recipe details. 
* Make sure so `only` the author can edit the recipe. 
* Make sure so `only` the author can delete the recipe. 
* Make sure that my `delete modal` is appearing when the author of the specific recipe choose to delete it. 

### Add Recipe

I have manualy tested so the elements of this page works correct: 

* Make sure so the recipe `slug` was unique for each recipe like a `ID`. 
* Make sure so the user gets a warning message is the user tries to add a recipe with the same title as another recipe. 
* Make sure so a user can't add unrealistic numbers for the cooking process like, for how many `Serves` this message will appear `Ensure this value is less than or equal to 14.`, 
for how long `Prep time` this message will appear `Ensure this value is less than or equal to 100.` and for 
`Cook time` this message will appear `Ensure this value is less than or equal to 300.`. 
* Make sure that add recipe and edit recipe get saved to the list of recipes. 

### Authentication

I have manualy tested so the authentication for each page works correct: 

* Make sure so the `Login` page only accepts the correct username and password, and then directs the user back to the home page. 
* Make sure so the `Logout` page appears with `You are about to sign out. Is that what you want?` message and then directs the user back to the home page. 
* Make sure so the `Sign up` page works correctly and directs the user back to the home page. 

### About Modal

I have manualy tested so the about modal works correct: 

* Make sure so the `About` nav link opens the modal.  
* Make sure so the about modal can be closed by `Press outside the modal, The "X" in the right corner or The "Close" button`. 

### My favorites

I have manualy tested so these functions and elements works correct:

* Make sure so the `My favorites` is shown only for logged in users and that it directs the user to `{username} favorite recipes` page. 
* Make sure so the `Bookmark recipe` button on the `Recipe detail` page is working as it should, and so the success message appears. 
* Make sure so the `Remove bookmark` button on the recipe at the `My favorites` page works and removes the recipe from that list but doesn't get deleted totally. 
* Make sure so a user can't duplicate favorites by adding the same recipe several times to `My favorites`. 
* Make sure so a user can't manually type in a page number that doesn't exists for the `page pagination` to trigger an error. 


---
## Defensive Programming

After my second session with my mentor [Benjamin Kavanagh](https://github.com/BAK2K3) (link) I got the feedback that I should implement `Defensive Programming` for my `CRUD functionality` which stands for `Create, Read, Update, Delete` and that is translated to my `Add recipe for "Create", Edit recipe for "Update", Delete recipe for "Delete"`. The `Read functionality` is just the way a guest or user can view a recipe, but that isn't a part of `Defensive Programming` since you doesn't need to be authenticated to view the recipes. 

So on to what I did to improve my backend code the way I did in the front end code is that I added a `@login_required` decorator that is a part of `Django decorators` (read more about django decorators [here](https://docs.djangoproject.com/en/dev/topics/auth/default/#the-login-required-decorator) (link)), to ensure that what ever guest or user that is trying to access either `Add recipe, Edit recipe, Delete recipe, Bookmark recipe, Remove bookmark` is authenticated. 

For my `Edit recipe and Delete recipe` I wanted to make sure that only the `author` (creator of that recipe) could `Edit or Delete` the specific recipe, otherwise the guest or user would be directed to my custom `403 error page`.

**Here are some screenshots of my function based views in views.py for my recipes app:** 

**Add recipe:**

![Screenshot of function based views in views.py in recipes app, add_recipe](/assets/readme/testing-readme/add_recipe.png)

**Edit recipe:**

![Screenshot of function based views in views.py in recipes app, add_recipe](/assets/readme/testing-readme/edit_recipe.png)

**Delete recipe:**

![Screenshot of function based views in views.py in recipes app, add_recipe](/assets/readme/testing-readme/delete_recipe.png)

**Here are a screenshot of my function based views in views.py for my profiles app:**

![Screenshot of function based views in views.py in profiles app, remove_favorite and add_favorite](/assets/readme/testing-readme/profiles-views.png)


---
## Automated Tests

For this project I have not done any `Automated tests`, because my knowledge for automated tests in django wasn't enough for me to try. I was too focused on learning `Django` and complete this project. But now when I feel more confident with `Django` and understands it better I will perform these tests for my future projects.  


---
## RETURN BACK TO [TOP](#testing)