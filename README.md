# What To Eat 

What To Eat is a recipe website where both first time visitors and users can see all of our delicous recipes. 
If a visitor wish to share their own delicous recipes, they can do so by register for a free user account. Old 
users can login/logout, see all of the recipes, edit or delete the recipes that they have created.  

### HINT:
**Remember that all links in this Readme does not open in a new tab. They open in this window. I have added a "(link)" to remember you as a reader that "this is a link", so you easier can remember that each link opens in this window.**  

![Screenshot of Techsini mockup](/assets/readme/design/project-image.png)

To visit `What To Eat` website please click this [link](https://whattoeat2022.herokuapp.com/) (link).


---
## Portfolio Project Four

### Intention 

This website is a fictional website for the purpose of my Fourth Portfolio Project for Code Institute’s Full Stack Software Development Course. I created this website with the knowledge I gained from the `Bootstrap, Django` modules.

The main goal of this project was to test my new knowledge in Django and Bootstrap. I decided to create a 
recipe website beacuse I am a food lover and tought that I could have some use for it myself. 

##### Features I aimed to achieve with this project:

* To make the website `easy` to understand for the user. 
* Make sure that the website has good `UI and UX` throughout the whole website so the user doesn't get confuesed. 
* Inspire people with recipes that they could eat for dinner. 


---
## How To Navigate The Website 

This website consists of a navbar on top, with the `logo, about, register, login, add recipe, my favorites` for both first time visitors or user's that has an account. But `Add recipe` will only be available to use for user's which are logged in otherwise a message will appear which tells the visitor to `register or login`. 
`My favorites` will only be displayed for authenticated users.

A first time visitor or user will find all of the recipes listed on the start page, the recipes are listed with `pagination` of 6. So more then 6 recipes will then be displayed on a `"new page"` which can be accessed by a `Next` button, on the new page there will be a `Previous` button. 

If a visitor or user selects a specific recipe to click on they will be directed to a page that hold the recipe details. The only difference in design of this page is if the visitor/user is authenticated and then a `Edit and Delete recipe` button will appear for user's who added their recipe. 

In the footer of the page the social media links can be found, but also the copyright symbol of What To Eat.

`About` What To Eat link will trigger a `"pop-up modal"` with information about the website. 

`Register and login` looks almost the same apart from some design features that are necessary. 

`Add recipe or Edit recipe` which are available for logged in users shares the same design apart from some buttons and headings.

`My favorites` will be available for logged in users. When a user `View recipe` they can choose to `Bookmark recipe` to add it to their favorites. If they wish to remove a recipe they can do so by click `Remove bookamrk` on the specific recipe card.  

I hope that you will find some delicous recipes when navigating the website. 


---
## Table of Contents

* [Planning](#planning)
  * [Wireframe](#what-to-eat---balsamiq-wireframe)
  * [Trello](#trello---user-stories-board)

* [UX](#ux) 
  * [User Stories](#user-stories) 
  * [Strategy](#strategy)
  * [Scope](#scope) 

* [Website Design](#website-design)
  * [Design](#design)
  * [Colors](#color-scheme)
  * [Fonts](#fonts)

* [Logic](#logic) 
  * [Flow Diagram](#flow-diagram)
  * [Explain Logic in Flow Diagram](#explain-logic-in-flow-chart) 
  * [Database Diagram](#database-diagram)
   
* [Existing Features](#existing-features)
  * [Start Screen](#start-screen)
  * [Recipe List](#recipe-list)
  * [View Recipe Details](#view-recipe-details)
  * [Footer](#footer)
  * [Navbar](#navbar)
  * [About modal](#about-modal)
  * [Add recipe not logged in](#add-recipe-not-logged-in)
  * [Add recipe logged in](#add-recipe-logged-in)
  * [Edit recipe logged in](#edit-recipe-logged-in)
  * [Register](#register)
  * [Login / Logout](#login-logout)

* [Testing](#testing)
  * [Bugs](#bugs)

* [Technologies Used](#technologies)

* [Credits](#credits)

* [Deployment](#deployment)
  * [GitHub & Gitpod ](#github--gitpod)
  * [Forking GitHub Repository](#forking-github-repository)
  * [Cloning GitHub Repository](#cloning-github-repository)
  * [Heroku](#heroku)

* [Support](#support) 


---
## Planning

### What To Eat - Balsamiq Wireframe

I created a Wireframe for this project to showcase for my mentor what my design idea for this project would look like using [Balsamiq - wireframes](https://balsamiq.com/) (link). But I also created this so I could focus more on designing the actual website instead of having to think to much how the design for this project would look. 

Instead adding all scrrenshots of my wireframe here I have decided that you can take a look at it by this shared link of my wireframe, [What To Eat - wireframe](https://balsamiq.cloud/sxp607p/pbhbjfz) (link).

### Trello - User Stories Board

Before I started to work with the code for this project I was requested of my mentor to create a mapping tool for my `user stories` to easier track `what to do when`. So I choose to use `Trello` as my tool for this. During my development I have been moving each user story with it's `EPICS` to the correct stage of the process, and I have made sure that each user story was manualy tested and fully functional before moving on to the next one. 

If you want to visit my trello board you can do so by visit this [link](https://trello.com/b/Hy1ZJoPK/portfolio-project-4) (link).

I will demonstrate for you down below each step of my trello board during my development:

**Trello board:**

![Screenshot of trello board](/assets/readme/planning/trello.png)


**To Do (Admin):**

![Screenshot of trello admin to do](/assets/readme/planning/todo-admin.png)

**In-design (Admin):** 

![Screenshot of trello admin in-design](/assets/readme/planning/indesign-admin.png)

**Testing (Admin):**

![Screenshot of trello admin testing](/assets/readme/planning/test-admin.png)

**Done (Admin):**

![Screenshot of trello admin done](/assets/readme/planning/done-admin.png)

Then I have been doing this for each and everyone of the rest in my `To Do` list. I have displayed the other ones in my `To Do` list underneath: 

![Screenshot of trello to do epics: recipe list and user authentication](/assets/readme/planning/todo1.png)

![Screenshot of trello to do epic: recipes](/assets/readme/planning/todo2.png)

![Screenshot of trello to do epic: learn about the website](/assets/readme/planning/todo3.png)


---
## UX 

#### User Stories
As a guest I would like to be able to: 

* Register an account using username, email, and password.
* Learn more about the website.
* Visit the website's social platforms. 
* View all of the recipes. 
* View the recipe details of a selected recipe. 

As a user I would like to be able to: 

* Login to my account. 
* Add recipes to the list of recipes. 
* Edit and delete recipes created by me. 

As a admin I need to be able to: 

* See the entire list of recipes that has been added. 
* Add recipes to the list of recipes to be viewed by everyone. 
* Edit and delete recipes created by admin. 
 
#### Strategy

* **Project Goal**
Create a website that allows users to create an account so they can see, add and edit recipes. 

#### Scope 

* A simple and straightforward UX experience.  
* A navigation bar that is easy to navigate the website with.
* A website that is compatible on most screen devices. 


---
## Website Design

### Design

`Logo design` - Because this website was created with the intention to keep it clean and simple. I decided to go with only `“What To Eat”`. Because I thought it gives the website a simple and clean look.

`Background Image` - I downloaded this image from pixabay.com which is a website with free images. And I used a white background color to it in case the image wouldn't load.

`Navigation bar` - I decided to use a pretty standard navbar with navigation links, but I think that gives the website a straight forward look. 

`Text over recipe list` - Here I choose to only have a `h1 header, a paragraph and a h2 header` for representing the recipe list.

`Recipe list` - The recipe list is paginated (sorted) in an order of 6 recipes per page, all amount over that will add the `Next and Previous` buttons. 

`Footer` - I choose a `footer` that would look similar to my navbar and contain just the most necessary information such as 
`a contact me header, my social media links and the what to eat copyright information.`

`About modal` - I didn't want to create a seperate page for the about information so therfore I choose to use a `modal` for this. 

`Add recipe` - This page is design in two different ways, either with only a message that says that you will have to login or register for an account, or a form with all the infromation that is required for adding a recipe. 

`Edit recipe` - Is designed the same way as `Add recipe` but it is tweaked with text to match `Edit recipe`. 

`My favorites` - Is designed with an `h1 header` on top with the users name and favorite recipes. The favorite recipes list is displayed almost the same way as on the home page but they are paginated by 3 per page instead of 6. 

`Register` - Is just designed with the standard look that comes with `allauth`, I have only designed the `h1 font design to go with the rest`. 

`Login and Logout` - looks almost the same in there design and is almost standard looking with `allauth` with a matching header. 

`Buttons` - All buttons for the website is green to match each other except the delete button which is red. 

`Summernote` - I used this to add the `"text tools"` to edit the information inside both the `ingredients and instructions` text boxes for add and edit a recipe. 

### Color Scheme 

I choose four colors for my website, `a lighter green for footer links and as an hover effect on the logo and nav links`, `a darker shade of green for the logo`, `a dark shade of green for all buttons`, `red for delete`, `black and white` for all text.   

**#34A56F - A lighter green (HEX-color)** 

![Screenshot of green color](/assets/readme/color/logo-green.png)

**#20603C - A darker green (HEX-color)** 

![Screenshot of green color](/assets/readme/color/%2320603C.png)

**#1C5434 - A dark green (HEX-color)** 

![Screenshot of green color](/assets/readme/color/%231C5434.png)

**Red color (Default bootstrap color "btn-danger")**

![Screenshot of red color](/assets/readme/color/red.png)

**Black color (Default css color)**

![Screenshot of black color](/assets/readme/color/black.png)

**#ffffff White color (Default css color), I haven't provided a image because of the white background it won't show.**


### Fonts

I choose two different fonts for my website, `"Dancing Script"` for my logo and all headings (h1, h2, h3) and `"Lato"` for all other text. I choose these two fonts because I thought they matched good togheter and for this website. The fonts were taken from `pairfonts.com`. 

**Dancing Script for my logo and all headings:**

![Screenshot of black color](/assets/readme/color/fonts/logo.png)

**Lato for all other text:**

![Screenshot of black color](/assets/readme/color/fonts/lato.png)


---
## Logic 

### What To Eat - Database Schema

Before I started to code this project I created a `Diagram Entity Relationship - Database Schema` using [dbdiagram](https://dbdiagram.io/home) (link). I created this to easier understand the database models that I was going to create for this project.

![Screenshot of database schema](/assets/readme/logic/db-schema.png)

### What To Eat - Flow Diagram

Before I started to write any code for this project I made sure to create an easy and straightforward `Flow Diagram` with all the logic for this project. The `Flow Diagram` was created with the use of 
[Lucid Chart](https://www.lucidchart.com/pages/) (link). I used the free version that is available for anyone that register an acount at their website. My `Flow Diagram` is demonstrated below. 

![Screenshot of flow diagram](/assets/readme/logic/flowdiagram.png)

**Explain flow diagram:** 

First the user visits the website as a guest, the first page the user sees is the `start page`. At the start page the guest is able learn more about the website or view all of the recipes. 

If the guest clicks on the `Add recipe` nav link, a page will appear that tells the guest to either login or register for an account to add recipes. 

If the login isn't approved the user will get a message above the login form that says `The username and/or password you specified are not correct` and the guest can try again. 
When the login is approved, the guest will then become a user and will be redirected to the `home page`. 

If the user choose to add a recipe, the recipe page will appear and the user can now add a recipe to the list of recipes. After the user has clicked on `Save` the user will be redirected to the `home page`. 

At the `home page` the user can view all recipes but also click on `View recipe` to see the recipes details, if the user is the creator or this recipe then the user is able to edit or delete the recipe. But if not the user can only view the recipe details.  

If the user choose to edit the recipe, the user will get directed to the `Edit recipe` page and after the user has clicked on `Save` the user will get redirected back to the `home page`. 

But If the user choose the `delete` button a delete modal will appear with a question if the user want to delete or not, if yes the recipe will be deleted permently and if not the user can close the modal window by the close button or just click somewhere outside the modal. 

When the user `View recipe` a recipe he or she can then choose to `Bookmark recipe` to add it to their `My favorites` recipes. If the user want to remove a recipe from the `My favorite` recipe he or she can do so by the red button that says `Remove bookmark` at each recipe card at their `My favorite` recipe list.  


---
## Existing Features

### Start Screen 

For the start page I choose a vertically aligned navigation bar on top, with all of the navigation links `About, Add recipe, Register, Login` or `About, Add recipe, My favorites, Login/Logout` if the user is authenticated. After that there is a background image with some text underneath that presents the list of recipes in the lower section of the page, this text will change slightly to create a personal welcome message for a user that is authenticated. At the bottom I have my `footer` with contact me and my social media links as well as copyright for 
`What To Eat`.
All other pages on the website inherits the navigation bar and footer.  

This is how it looks: 

**Not authenticated:**

![Screenshot of start page upper part (not logged in)](/assets/readme/design/home.png) 

**Authenticated:**

![Screenshot of start page upper part (logged in)](/assets/readme/design/home2.png) 

**Not authenticated:**

![Screenshot of start page lower part (not logged in)](/assets/readme/design/home-down.png) 

**Authenticated:**

![Screenshot of start page lower part (logged in)](/assets/readme/design/home-down1.png) 

### Footer

**Footer:**

![Screenshot of footer](/assets/readme/design/footer.png) 

### Navbar

**Navbar links:**

The navbar links depends as I have mentioned earlier, either there is `About, Add recipe, Register, Login` or `About, Add recipe, My favorites, Login/Logout` if the user is authenticated. 

![Screenshot of navbar](/assets/readme/design/navbar.png)

![Screenshot of navbar logged in](/assets/readme/design/navbar1.png)

### About modal

**About modal:**

The about link will trigger a `modal` that contains the about What To Eat text. To close the about modal you can just click anywhere else outside it or use the close button. 

![Screenshot of about modal](/assets/readme/design/about-modal.png)

### Add recipe

**Add recipe:**

The `Add recipe` link will either display a `You have to login to add your own recipes!` message or the form for adding a recipe depending of if the user is authenticated or not on the that page. 

**Add recipe, not authenticated:**

![Screenshot of add recipe site not authenticated](/assets/readme/design/add-recipe.png)

**Add recipe, authenticated:**

![Screenshot of add recipe site authenticated](/assets/readme/design/add-recipe1.png)

### User

**Register account:**

The `Register` page displays a register your account page with `username, email (optional), password, password again`. 

![Screenshot of register an account](/assets/readme/design/register.png)

The `Login` page displays a login form and if the user is already authenicated (logged in) the `Logout` navigation link will trigger a page that says 
`You are about to sign out. Is that what you want?` with a confirmation button to sign out. 

**Login:**

![Screenshot of login page](/assets/readme/design/sign-in.png)

**Logout:**

![Screenshot of logout page](/assets/readme/design/sign-out.png)

### Recipes

**Recipe card:**

![Screenshot of recipe card](/assets/readme/design/recipe-card.png) 

**Next and previous page:**
When there are more then 6 recipes in `What To Eat's` recipe list a `"Next"` button will appear that takes the user or site visitor to the next page of recipes which loads with the same 
content as the start page to match, and then a `"Previous"` button will replace the `"Next"` button so the user can get back to the start page. The list of recipes is in an order of newest to oldest.  

![Screenshot of next button](/assets/readme/design/next.png)

![Screenshot of previous button](/assets/readme/design/previous.png)  

**View recipe:**

When a `user` has selected a recipe to view by clicking `View recipe` from the recipe list, a detailed page of that recipe will appear with the recipe name on top, the created on and by information underneath. Right below that there is an image of the recipe, which can be selected by a user of what ever image they would like or a standard image will be provided. On the right there is two boxes on top of eachother `Recipe details` and `ingredients`. `Cook method` is found right underneath the recipe image. And if the user is authenticated and is the creator of the specific recipe he or she can then edit or delete the recipe by a green and red button on the bottom of the `Recipe details` page. 

**Recipe details, not authenticated or creator of recipe:**

![Screenshot of recipe details, not logged in or creator of recipe](/assets/readme/design/recipe-detail.png)

**Recipe details, authenticated:**

![Screenshot of recipe details, logged in](/assets/readme/design/recipe-detail1.png)

If a user is logged in, he or she can then see the `Bookmark recipe` button for each recipe and then add it to the `My favorites` recipe page. 

**Recipe details, authenticated and creator of recipe:**

![Screenshot of recipe details, logged in and creator of recipe](/assets/readme/design/recipe-detail2.png)

### Edit recipe

If the user is the creator of the recipe and wish to `edit` the recipe he or she can then click the green button that says `Edit recipe` to come to the edit recipe page, this page looks 
similar to the `Add recipe` page but each input field will be filled out with the recipe information of that recipe. 

**Edit recipe, authenticated and creator of recipe:**

![Screenshot of edit recipe](/assets/readme/design/edit-recipe.png)

### Delete recipe

If the user is the creator of the recipe and wish to `delete` the recipe he or she can then click on the red button that says `Delete recipe`. A modal will then appear on the top of the page to inform the user that he or she is about to delete the recipe and asks for a confirmation on this. 

**Delete recipe, authenticated and creator of recipe:**

![Screenshot of delete recipe modal](/assets/readme/design/delete-recipe.png)

### My favorites

**My favorites recipe page:**

![Screenshot of my favorite recipes, remove bookmark](/assets/readme/design/remove-favorite.png)

Here the user can remove each bookmarked recipe by pressing the `Remove bookmark` button on each recipe. 


---
## Future Features 

A feature that I would like to add in the future is the ability to categorize the protein source into `meat, fish, vegetarian or just a mix of all`. This is a feature that I felt I didn't have the knowledge or time for to create, but therfore I have decided to leave it as a future feature for me to add to this project. 

Another feature that I would like to add is a random function like a seperate page where authenticated users could randomly generate a meal from the list of all recipes, of course from the protein source that they have specified and then add this meal for their week's list. This list will then be saved for them to check for `what to eat` for each day of the week. And then they can remove items aswell from that list so they can create a new one for next week etc. 


---
## Technologies

Technologies that I used for `What To Eat` website project is the following down below.

#### Programming Languages 

* [Python 3](https://www.python.org/) (link): Python is a general-purpose language, meaning it can be used to create a variety of different programs and isn't specialized for any specific problems.

#### Frameworks & Programs 

* [Django](https://www.djangoproject.com/) (link): Django is a high-level `Python web framework` that enables rapid development of secure and maintainable websites.

* [Bootstrap 5](https://getbootstrap.com/) (link): Bootstrap is a `CSS framework and toolkit`. Developers can't use it to write programs, but because Bootstrap contains massive amounts of reusable code and website element templates, the framework can remove some of the “busy work” and significantly speed up the process of building a website. 

* [GitHub](https://github.com) (link): GitHub is used to store all data from the project after it has been pushed using the 
`git add . | git commit -m "message here" | git push` command in the GitPod terminal. 

* [GitPod](https://www.gitpod.io) (link): I used `GitPod` as my `IDE` that stands for `An integrated development environment (IDE) is a software for building applications that combines common developer tools into a single graphical user interface (GUI)`. You can read more about this [here](https://www.gitpod.io/blog/gitpod-launch) (link). 

* `Git`: This is used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub. Incase someting unexpected happens to your gitpod workspace, everything is committed to your GitHub repository. 

* [Heroku](https://www.heroku.com) (link): Heroku is a container-based cloud Platform as a Service `(PaaS)`. Developers use Heroku to deploy, manage, and scale modern apps.

* [LucidChart](https://www.lucidchart.com/pages/) (link): Lucidchart is the intelligent diagramming application that empowers teams to clarify complexity, logic and more. To get a better visual understanding about how an application work. 

* [PEP8](http://pep8online.com/) (link): Is a validation tool that I used to validate my code. 

* [Techsini](https://techsini.com/multi-mockup/index.php) (link). Used to create the mockup image. 

* [Font Awesome](https://fontawesome.com/) (link). Was used to add icons for my social media links. 

* [Pair Fonts](https://pairfonts.com/) (link). I used Pair Fonts to add custome fonts for the aesthetic and UX purposes. 

* [Balsamiq](https://balsamiq.com/) (link). Balsamiq was used to create my wireframe for my design process. 

* [dbdiagram](https://dbdiagram.io/home) (link). dbdiagram was used to create my database schema before I started to code my project. 

* [Trello](https://trello.com/) (link). Trello was used for creating my board for mapping my user stories in this project.

* [Favicon](https://favicon.io/) (link). Favicon was used to create the little icon that is showing in the browser adress bar to make the user experience more professional for the website. 


---
## Testing

All testing of this project has been documented in a seperate file called `TESTING.md` and you can fin it [here](TESTING.md) (internal link). 

### Bugs 
 
* **Bug 1:**
Success message that shows that user is `logged in/logged out`.
When a user login/logout a green message will appear to clarify that the user is `logged in/logged out`. But it didn't go away after the `3000` milliseconds
I had in my JavaScript function. It stayed at the top of the page until I refreshed it.
Like shown in the screenshot below:

**Screenshot:**

![Screenshot bug 1](/assets/readme/bugs/bug1.png)

* **Solution Bug 1:**
It was as simple as that I had choosen the wrong `Bootstrap` version as well as I hadn't added a `Bootstrap` version for `JavaScript`. 
The version I first had was `Bootstrap 5.0.2` for only `Bootstrap`. 
I changed `Bootstrap version` to `Bootstrap 5.0.1` and added the `Bootstrap JavaScript 5.0.1` link. 

* **Bug 2:** 
My modals for the `About link and Delete recipe button` wasn't appearing when clicking on respective button/link. 

* **Solution Bug 2:**
The same solution was for bug 2 as bug 1, my modals started to working after I added the `Bootstrap 5.0.1` version and added the `Bootstrap JavaScript 5.0.1` link.

* **Bug 3:** 
My footer wasn't at the bottom of the page. When I clicked on register/login/logout etc my `footer` was not at the bottom of the page, it was right underneath the content of each 
page. Like shown in the screenshot below:

**Screenshot:**

![Screenshot bug 3](/assets/readme/bugs/bug3.png)

* **Solution Bug 3:**
I made a search on google and found this [website](https://radu.link/make-footer-stay-bottom-page-bootstrap/)(link) with a two step method. So I just added
a class of `d-flex flex-column min-vh-100` to the `body` in my base.html file. 

### Unfixed Bugs

For some reason is the textfields for ingredients and instructions at `add recipe and edit recipe pages` not the same width as the `Excerpt and Title`. It doesn't affect desktop users that much but mobile users will have to scroll to the side to cover the whole textarea and reach all of the tools to modify the text. I have tried to fix this without success so I will leave it as an unfixed bug for now.  


---
## Credits

#### Media 

All images for this project was taken from [Pixabay](https://pixabay.com/) (link). 

#### Inspiration for this project

[Code Institute](https://codeinstitute.net/) (link) - I took inspiration to this project from the `Code Institute` videos of `I Think Therefore I Blog`. 

[Best Beer Project - by nandabritto (other student)](https://github.com/nandabritto/beer_rate) (link) - I took some inspiration from this project to 
create some of my `Django` and `Bootstrap` functionality. 

[Lettuce Eat Project - by Kat632 (other student)](https://github.com/Kat632/PP4-LettuceEat) (link) - I took some inspiration from this project to create the view of my recipe list and the forms for add recipe and edit recipe.  

#### Help from Stack Overflow

At first I had an issue that when paginate (press next and previous) in the recipe list on the home page, a user could manually type in a random number in the adress bar like shown in the image below to trigger a 404 page. To prevent this I used a solution found on `Stack Overflow` provided to me by my mentor [Benjamin Kavanagh](https://github.com/BAK2K3) (link), the solution can be found via this [link](https://stackoverflow.com/questions/40835222/display-last-page-of-paginated-results-instead-of-404-using-listview) (link). I just wrote the exact same code as written by `TimB` among those answers and it solved my issue. 

![Screenshot adressbar manually paginate random wrong number](/assets/readme/wrong-page.png)

**Here is the code that solved my problem:**

![Screenshot code solution for wrong pagination](/assets/readme/paginate-wrong.png)


---
## Deployment 

**GitHub:**

I frequently used `commit` throughout the whole project, this is the commands used in the terminal: 

* `git add .` (This command is used for adding files to the staging area before committing).
* `git commit -m “commit message here..”` (This is used to label the commit changes made to the local repository).
* `git push` (This command is used to push all changes to the Github repository). 

This is all done to prevent any `data` loss in case Gitpod crashes and saves the `data` to GitHub. 


### GitHub & Gitpod 

For this project I used Code Institutes Python template that can be found [here](https://github.com/Code-Institute-Org/python-essentials-template) (link). 

**Steps to create a new repository in Github:**

1. Sign in or sign up to [GitHub](https://github.com) (link). 
1. When you have done that, you will see `"new"` up in the left corner. 
**Like this:**
![Screenshot new repository button github](/assets/readme/github.png)
1. Select in the dropdown menu under `Repository template` if you for example would like to use the template provided by `Code Institute` that I did for this project. If you don't see it in the dropdown menu click this [link](https://github.com/Code-Institute-Org/python-essentials-template) (link) to get to the one provided by `Code Institute` and click `Use this template` to the left of the green Gitpod button.
1. When you have done that, give the repository a name. Leave it public if you want anyone on the internet to see your repository (I always do). 
1. Click create repository. 
1. **Remember** to use the `commit` commands that I explained above so your hard work doesn't get lost if anything happens to Gitpod. 

### Forking GitHub Repository

Forking a Github repository is the process of making a copy of someone else repository and add your own changes to it without changing the original, the original repository is known 
as "upstream repository". I will explain the process of forking down below: 

1. Go to the Github page that hosts the repository you wish to fork. 
1. In the top-right corner of the page there is a button that says `"Fork"`. 
1. Click this button. 
1. This creates a copy of that repository to your Github home page. You can submit and receive changes to your copy by using pull requests and/or syncing with the original upstream repository. 

This instructions were taken from [Github - Fork a repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo) (link). 

### Cloning GitHub Repository

Cloning a repository inolves making a full copy of a repository on your local machine. This allows you to work on the code easier. Changes can be pushed back up to the Github site or changes from other sources pulled to your local copy. I will explain how to clone down below: 

1. Go to the repository page on Github. 
1. Above the file list click on the green button that says `"Code"`. 
1. You can choose to download a zip file of the repository, to unpack it on your local machine and open it in your IDE. 
1. Clone using HTTPS by copying the URL under the HTTPS tab. 
1. Open a terminal window, set current directory to the one you want to contain the clone from. 
1. Type `git clone` and paste the URL copied from the Github page. 
1. The repository clone will now be created on your machine. 

This instructions were taken from [Github - cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) (link).

### Heroku 

Deploying a project using Heroku: 

* Don't forget to set your `DEBUG` in your `settings.py` file of your main app in `Django` to `False`.
* Ensure that all of your project dependencies are listed in the `requirments.txt` file. 
* If not, then you can use this command in the Gitpod terminal: `pip3 freeze --local > requirments.txt`.
* Visit the [Heroku](https://www.heroku.com) (link) website and click on create an account. 
* Click the `"New"` button. 
* Click the `"Create new app"` button. 
* Provide a name for the app in the `App` name input field. 
* Select your region from the `"choose region"` dropdown menu. 
* Click the `"Create App"` button. 
* Once redirected, proceed to the settings tab. 
* Click on the `"config vars"` button. 
* Supply a `KEY` of `PORT` and it's value of `8000`. Then click the `"add"` button. Do this with `Cloudinary, Database URL (from Heroku-Postgres) and your secret key`. 
* Next step is to add `Buildpacks`, click the `"Add Buildpack"` button. 
* The `Heroku Postgress` buildpack need to be added. 
* Once the buildpack have completed, go to the deploy tab, once on the deploy screen, select GitHub as the deployment method and connect your GitHub profile. 
* Search for the repository that you wish to deploy to `Heroku` and click `"connect"`. 
* Once your repository is connected to Heroku you can choose to either automatically or manually deploy your app.  
* By selecting automatic deploy, Heroku will build a new version of the app each time a change has been made and pushed to the repository on `GitHub`. 
* Click on manual deploy to build your App. When complete, click on `View` to open up the live site on `Heroku`.  
* Finished. 

If the `create app` process at `Heroku` website wouldn't work follow these steps: 
* When you want to deploy your project to `Heroku`. 
* Type `heroku login -i` to login to your existing account (if you have one) in the `Gitpod` terminal. 
* Then run the command `heroku create your_app_name_here` to create a new app (the name has to be uniqe). 
* Now you can see your new project at `Heroku` dashboard and set the config vars and buildpacks as the steps explained above. 


---
## Support 

I would like to give an extra `Thank you` to all the kind people I have around me that gave me support in all different ways. 

* **Code Institute** for their **Tutor** support. 
* My mentor [Benjamin Kavanagh](https://github.com/BAK2K3) (link) for being a **Superior** mentor.
* **Google** for always clear things up.
* **Code Institute Slack channel** for always helping out with problems or questions. 
* My lovely **Girlfriend** for always supporting and believing in me.

### RETURN TO THE [TOP](#what-to-eat)
