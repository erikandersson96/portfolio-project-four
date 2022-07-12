# Testing 

During my development for this project each function were tested to work as expected. Each section in this file describes all of the different tests. 


---
## Table of contents - testing

* [Validation Testing](#validation-testing)

* [User Story Testing](#user-story-testing)

* [Device Testing](#)

* [Manual Testing](#)

* [Automated Testing](#)


---
## Validation Testing


---
## User Story Testing


---
## Device Testing


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
## Automated Testing


---
## RETURN BACK TO THE [TOP](#testing)