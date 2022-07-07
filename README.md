# What To Eat 

What To Eat is a recipe website where both first time visitors and users can see all of our delicous recipes. 
If a visitor wish to share their own delicous recipes, they can do so by register for a free user account. Old 
users can login/logout, see all of the recipes, edit or delete the recipes that they have created.  

**Remember that all links in this Readme does not open in a new tab. They open in the same window.** 

To visit What To Eat website please click this [link](). 

![Screenshot of I am responsive]()


---
## Portfolio Project Four

### Intention 

This website is a fictional website for the purpose of my Fourth Portfolio Project for Code Institute’s Full Stack Software Development Course. I created this website with the knowledge I gained from the `Bootstrap, jQuery, Django` modules.

The main goal of this project was to test my new knowledge in Django and Bootstrap. I decided to create a 
recipe website beacuse I am a food lover and tought that I could have some use for it myself. 

##### Features I aimed to achieve with this project:

* To make the website `easy` to understand for the user. 
* Make sure that the website has good `UI and UX` through out the whole site so the user doesn't get confuesed. 
* To make it easier for people to decide what they should eat for dinner. 


---
## How To Navigate The Website 

This website consists of a navbar on top, with the `logo, about, register, login, add recipe` for both first time visitors or user's that has an account. But `Add recipe` will only be available to use for user's which are logged in otherwise a
message will appear which tells the visitor to `register or login`. 

A first time visitor or user will find all of the recipes listed on the start page, the recipes are listed with `pagination` of 6. So more then 6 recipes will then be displayed on a `"new page"` which can be accessed by a `Next` 
button, on the new page there will be a `Previous` button. 

If a visitor or user selects a specific recipe to click on they will be directed to a page that hold the recipe details. The only difference in design of this page is if the visitor/user is authenticated and then a `Edit and Delete recipe` button will appear for user's who added their recipe. 

In the footer of the page the social media links can be found, but also the copyright symbol of What To Eat.

`About` What To Eat link will trigger a `"pop-up modal"` with information about the website. 

`Register and login` looks almost the same apart from some design features that are necessary. 

`Add recipe or Edit recipe` which are available for logged in users shares the same design apart from some buttons and headings.

I hope that you will find some delicous recipes when navigating the website. 


---
## Table of Contents

* [UX](#ux) 
  * [User Stories](#user-stories) 
  * [Strategy](#strategy)
  * [Scope](#scope) 

* [Website Design](#website-design)

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
  * [Manual Testing](#manual-testing)
  * [Automated Testing](#automated-testing)
  * [Bugs](#bugs)
  * [Validation](#validation)
  * [User Story Testing](#user-story-testing)
  * [Device Testing](#device-testing)

* [Technologies Used](#technologies-used)

* [Content](#content)

* [Credits](#credits)

* [Deployment](#deployment)

* [Support](#support) 


---
## UX 

#### User Stories
* 
* 
* 
* 
 
#### Strategy

* **Project Goal**
Create a website that allows users to see, add and edit recipes. 

#### Scope 

* A simple and straightforward UX experience.  
* A navigation bar that is easy to navigate the website with.
* A website that is compatible on most screen devices. 


---
## Website Design

For the start page I choose a vertically aligned navigation bar on top, with all of the navigation links `About, Add recipe, Register, Login` or just `About, Add recipe, Login/Logout` if the user is authenticated. After that there is a background image with some text underneath that presents the list of recipes in the lower section of the page, this text will change slightly to create a personal welcome message for a user that is authenticated. At the bottom I have my `footer` with contact me and my social media links as well as copyright for `What To Eat`.
All other pages on the website inherits the navigation bar and footer.  

This is how it looks: 

![Screenshot of start page upper part]() 

![Screenshot of start page lower part]() 

When there are more then 6 recipes in `What To Eat's` recipe list a `"Next"` button will appear that takes the user or site visitor to the next page of recipes which loads with the same 
content as the start page to match, and then a `"Previous"` button will replace the `"Next"` button so the user can get back to the start page. The list of recipes is in an order of newest to oldest.  

![Screenshot of next and previous buttons]() 

The about link will trigger a `modal` that contains the about What To Eat text. To close the about modal you can just click anywhere else outside it or use the close button. 

![Screenshot of about modal]()

The `Add recipe` link will either display a `You have to login to add your own recipes!` message or the form for adding a recipe depending of if the user is authenticated or not on the that page. 

![Screenshot of add recipe site not authenticated]()

![Screenshot of add recipe site authenticated]()

The `Register` page displays a register your account page with `username, email (optional), password, password again`. 

![Screenshot of register an account]()

The `Login` page displays a login form and if the user is already authenicated (logged in) the `Logout` navigation link will trigger a page that says 
`You are about to sign out. Is that what you want?` with a confirmation button to sign out. 

![Screenshot of login page]()

![Screenshot of logout page]()

When a `user` has selected a recipe to view by clicking `View recipe` from the recipe list, a detailed page of that recipe will appear with the recipe name on top, the created on and by information underneath. Right below that there is an image of the recipe, which can be selected by a user of what ever image they would like or a standard image will be provided. On the right there is two boxes on top of eachother `Recipe details` and `ingredients`. `Cook method` is found right underneath the recipe image. And if the user is authenticated and is the creator of the specific recipe he or she can then edit or delete the recipe by a green and red button on the bottom of the `Recipe details` page. 

![Screenshot of recipe details, not logged in or creator of recipe]()

![Screenshot of recipe details, logged in and creator of recipe]()

If the user is the creator of the recipe and wish to `edit` the recipe he or she can then click the green button that says `Edit recipe` to come to the edit recipe page, this page looks 
similar to the `Add recipe` page but each input field will be filled out with the recipe information of that recipe. 

![Screenshot of edit recipe]()

If the user is the creator of the recipe and wish to `delete` the recipe he or she can then click on the red button that says `Delete recipe`. A modal will then appear on the top of the page to inform the user that he or she is about to delete the recipe and asks for a confirmation on this. 

![Screenshot of delete recipe modal]()


---
## Logic 

### Flow Diagram 

Before I started to write any code for this project I made sure to create an easy and straightforward `Flow Diagram` with all the logic for this Quiz. The `Flow Diagram` was created with the use of 
[Lucid Chart](https://www.lucidchart.com/pages/) (link). I used the free version that is available for anyone that register an acount at their website. My `Flow Diagram` is demonstrated below. 

![Screenshot of my flow diagram first part]() 
![Screenshot of my flow diagram last part]()

### Explain Logic in Flow Chart

First the user starts the program. Secondly the user gets to the `Menu` with 3 options `Start Quiz | Leaderboard | Game Rules`. 

If the user choose `Leaderboard` the user will be displayed with the leaderboard stats and when the user wants to get back to the `Menu` the user just type `m or M`. If the user types an invalid input (not m or M) a message will appear with instructions about this. 

If the user choose `Game Rules` the user will be displayed the game rules and when the user wants to get back to the `Menu` the same principle works as for `Leaderboard` type `m or M` with the same message for invalid inputs. 

If the user choose `Start Quiz` the user will be asked for a `username`, the user can input anything (alphabetic only) maximum of 10 characters. If the user types the wrong character a message with instructions will appear to guide the user right in order to continue the Quiz. 

When the user has inputted a valid `username` the user will be asked for how many question that he or she would like to play `6 or 12`, the user can only input 6 or 12 as a valid input otherwise a message with instructions will appear that guides the user on how to continue. 

After this question the Quiz will start, when the user gets displayed with a question the user gets 2 options for the only one correct answer, this will be listed as `1 or 2`. If the user types anything else then 1 or 2 a message will appear with instructions about how to continue the Quiz. If the user answers correct he or she will be rewarded with +1 point. If the user answers incorrect he or she will not get any point. The loop with questions will continue until all questions has been displayed of the selected amount `6 or 12`. 

When the user has finsihed all questions of the amount that the user selected a `End Message` will appear with the users `username and total score`. 

To continue the user has to `Please press enter to continue...` to get a final question if he or she would like to either `play again` or `exit` the program by answer `Yes or No` by typing `y or Y` for Yes and `n or N` for no. If the user types anything else here a message with instructions will appear to guide the user to the correct input. If the user types `Yes` he or she will be taken back to the `Menu` with options or the program will exit if the user types `No`. 


---
## Existing Features

### Start Screen 

When the program starts the user will get a `Welcome message` including a `"Banner"` and a menu of three different options `Start Quiz | Leaderboard | Game Rules`. Underneath the menu the user can find the instructions about how to select the different options from the menu. See the screenshot below:

![Screenshot of start screen]()

If the user doesn't care to follow the instructions or accidentally types the wrong character instead a message will appear to inform the user that he or she has to try again with a valid input. See the screenshot below:  

![Screenshot of error message wrong input start screen]()

### Leaderboard & Game Rules

When the user selects the `Leaderboard` option he or she will see a leaderboard containing the top 3 finishers of the two different question selections either 6 or 12. When the user want's to exit the leaderboard an get back to the menu there is instructions below that explains this. See the screenshot below:

![Screenshot of leaderboard]()

When the user selects the `Game Rules` option he or she will first get a message that welcomes the user to the Game Rules, after that all of the Game Rules will be displayed. When the user want to exit the Game Rules and get back to the menu there is instructions below that explains this. See the screenshot below:

![Screenshot of Game Rules]()

When the user want to exit the `Leaderboard or Game Rules` to get back to the menu and accidentally types the wrong character instead of `m or M` a message will appear to inform the user that he or she has to try again with a valid input. See the screenshot below:

![Screenshot of exit leaderboard or game rules]()

### Username 

When the user selects `Start Quiz` to start the quiz a message will appear that says that the user needs to fill in a username, some instructions underneath the first message will inform the user that the username can't be any longer then 10 characters, it can't inculde numbers or special characters. See the screenshot below:

![Screenshot of type in username]()

If the user selected a `valid username` this message will appear: 

![Screenshot of type in username]()

When the user types in his or her username and accidentally types anything else then alphabetics a message will appear to inform the user that he or she has to try again with a valid input. See the screenshot below:

![Screenshot of error when type in username]()

### Question Selection 

After the user has selected a valid `username` he or she will be asked how many questions to play either `6 or 12`. See the screenshot below:

![Screenshot of question selection]()

If the user types an invalid number or character not `6 or 12` a message will appear with instructions of how to continue. See the screenshot below:

![Screenshot of error message question selection]()

### Questions 

The `questions` in the Quiz will be displayed to the user right after that the user has selected a valid input between `6 or 12` for the question selection, the user can choose between two options for each question, but only one is the correct answer. See the screenshot below:

![Screenshot of question]()

If the user inputs the correct answer of `either 1 or 2` this message will appear. See the screenshot below:

![Screenshot of correct answer for question]() 

If the user inputs the wrong answer of `either 1 or 2` this message will appear. See the screenshot below:

![Screenshot of wrong answer for question]()

When the user `answers` the question he or she can only input either `1 or 2` as a valid answer for the question, if the user inputs anything else then one of these a message will appear with instructions of how to continue. See the screenshot below:

![Screenshot of error message question]()

### End Message

When the user has `completed` all questions of the selected amount `6 or 12 questions` a result message will appear to inform the user about how many points he or she got. The user will see underneath `Please press enter to continue...`. See the screenshot below:

![Screenshot of end message]()

### Play Again 

When the user has pressed enter a message will appear with a question to the user that ask the user if he or she wants to play again or quit the quiz. If the user choose to play again 
`Y (yes)` he or she will be directed back to the menu, if the user choose `N (no)` the quiz will exit. See the screenshot below:

![Screenshot of play again, yes or no]()

If the user input something else then `Y or N` a message will appear to inform the user that he or she needs to try again with a valid option. See the screenshot below:

![Screenshot of error message play again, yes or no]()


---
## Future Features 

A feature that I would like to add that I didn't have the time for to add to this project is the abilty to record the time that the user takes to answer each question. 
So the `Formula One Quiz` would have been a little more challenging amongst friends when they are playing against eachother and the also implement the time to the leaderboard. 
If I were to use this function I would need to use this combination `start_time = time.time() and end_time = time.time()`.  

Add some extra time delays for the correct or wrong answers for the user. But since `Heroku` updated their process for deployment I felt unsure about how to update my code push it and then create a new app with new config vars. I tried to do this but then my app wasn't created in some wierd way even when I followed the steps for manual deploy thru `Gitpod` terminal. 
The app might have some bad user experience now because the time delay is a bit short, but I am fully aware of it and I would have changed it if I knew how to solve this manual heroku deployment problem. When my experience gets better I will be better for improving this in the future for future projects. 


---
## Technologies

Technologies that I used for this `Formula One Quiz` is the following down below.

#### Programming Languages 

* [Python](https://www.python.org/) (link): Python is a general-purpose language, meaning it can be used to create a variety of different programs and isn't specialized for any specific problems.

#### Frameworks & Programs 

* [GitHub](https://github.com) (link): GitHub is used to store all data from the project after it has been pushed using the 
`git add . | git commit -m "message here" | git push` command in the GitPod terminal. 

* [GitPod](https://www.gitpod.io) (link): I used `GitPod` as my `IDE` that stands for `An integrated development environment (IDE) is a software for building applications that combines common developer tools into a single graphical user interface (GUI)`. You can read more about this [here](https://www.gitpod.io/blog/gitpod-launch) (link). 

* [Heroku](https://www.heroku.com) (link): Heroku is a container-based cloud Platform as a Service `(PaaS)`. Developers use Heroku to deploy, manage, and scale modern apps.

* [LucidChart](https://www.lucidchart.com/pages/) (link): Lucidchart is the intelligent diagramming application that empowers teams to clarify complexity, logic and more. To get a better visual understanding about how an application work. 

* [PEP8](http://pep8online.com/) (link): Is a validation tool that I used to validate my code. 


---
## Testing

### Manual Testing 
  
##### Input 

I have tested my program all the time with the wrong type of inputs like: 

* **Menu:** 
At the menu I have tried to input anything else then `s or S to start the quiz, l or L for leaderboard, r or R for game rules` and the program runs a message that says that I have typed  wrong input and have to try again with a correct one. 

* **Start Quiz:**
  * **Username:** When the game asks for a username it is expecting only alphabetics and maximun length of 10 characters (so no numbers or special characters!). If I try to type let say: 5 I get a message that says `Not longer then 10 characters. Written with numbers or special characters. Try again!`. Even if I try to write longer then 10 characters I get the same message.
  * **How many questions?:** When the game asks for how many questions I would like 6 or 12, if I then type in `5` or `a` I will get a message that says 
  `You didn't Type in '6 or 12'! Please choose only one.`. 
  * **Question:** When a question is displayed the game is expecting only 1 or 2 as valid inputs but if I try to input `3` or `Hello` I will get a message that says 
  `Only enter either '1 or 2'. You entered something else...`. 
  * **Play again, Yes or No:** At the final step of the game were it asks me if I want to play again or exit the game, if I then type in `Banana` or `1` I will get a message that says
  `You did not Type 'y or Y' for yes to play the quiz again or 'n or N' for no to exit the program. You typed something else, try again.`. 

* **Leaderboard:** When I choose the Leaderboard at the menu and then wish to get back to the Menu, I need to type m or M. But if I try to type something else like `hello` or `2` I will get a pop up message for 3 seconds that says `Did you really press 'm or M'? Try again!`. 

* **Game Rules:** When I choose the Game Rules at the Menu and then wish to get back to the Menu, I need to type m or M. But if I try something else I will get the same pop up message as in leaderboard. 

All checking for validation when expecting a user input works correctly as expected. 

##### Game Play

Throughout the whole development of this Quiz I have tested the game in the GitPod terminal to see that my functions are working as expected, but also to debugg my code if my program have not operated as I expected it to do. 

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


### Validation

When testing my code in [PEP8 Online](http://pep8online.com/) validation tool I got no errors except that I had no newline at the bottom of the file. But that was only me erasing the last line in `PEP8` before checking my code because I thought that was correct. But since `GitPod` wont let me save my file without erros unless I have a newline at the bottom. Now I have changed that but I want to show a screenshot of the first `PEP8` result and underneath I will show the fixed screenshot. See images below: 

**No Newline:**
![Screenshot PEP8 validation error]()

**With Newline:**
![Screenshot PEP8 validation no error]()
 

### User Story Testing 

To meet the expectations in the user stories. I have tested my python project for each of them.

1. **Goal** 
* A user's perspective: I want to easily understand the purpose of the website. 

**Result**
* By presenting the game with `"F1 QUIZ"` first and a welcome message that explains that says `"Welcome to this Formula One Quiz!"`, so the user quickly understand the purpose of this website (python project). 

2. **Goal**
* A user's perspective: I want the quiz to have clear instructions about how the game works.

**Result**
* By always presenting instructions below each step the user takes in the game. 

3. **Goal**
* A user's perspective: I want the game to always provide me with information about how many questions I have played and have left, also how many points I have scored.

**Result**
* By adding the functionality to see which question of the selected amount the user is on right above each question. When the user has answered a question and if the user is correct the total points scored will be displayed underneath, but also when the game is finished. 


### Device Testing 

Since this project is dependent to run in a mock terminal it is restricted to `desktop` use only, otherwise it will be a bad user experience on a smaller screen device. 


---
## Python Libraries 

**Python libraries used for this project:** 
* **Os:** I choose to import this one so that I could enable the possibility for me to create a function that works as `"clear()"`, so I could call it within other functions so the terminal clears other text that were displayed before. The same principle is used when using the terminal in other situations and you want to clear out all unnecessary text so you get a cleaner look. Here you can take a look at the website of [OS](https://docs.python.org/3/library/os.html) (link).
* **Time:** I choose to import time to be able to set time delays `(time.sleep(seconds))` within certain functions so the Quiz doesn't executes to fast for the user to be able read the information. Here you can take a look at the website of [Time](https://docs.python.org/3/library/time.html) (link).
* **Random:** I had to import random in order for me to generate a random order of the questions for the user. 
This Formula One Quiz was created with the intention to test peoples knowledge in the sport. A game that people can share among their friends and family to challenge each other's knowledge. Here you can take a look at the website of [Random](https://docs.python.org/3/library/random.html) (link).
* **Pyfiglet:** I choose to import [pyfiglet](https://pypi.org/project/pyfiglet/0.7/) (link) so I could display `"F1 QUIZ"` in a 3d look without the need to create it myself. Take a look at their website to get all of the instructions to how you can implement it your self to your next python project. 


---
## Content

#### Media 

The `Ferrari red` color for the background was taken from [color-hex](https://www.color-hex.com/color/a6051a) (link), you can take a look at the color at their website by cliking the link. 

#### Footer 

The `footer` with the icons for the different social media links was taken from [Font Awesome](https://fontawesome.com/) (link).


---
## Credits

#### Code 

My mentor [Benjamin Kavanagh](https://github.com/BAK2K3) suggested me to use [pyfiglet](https://pypi.org/project/pyfiglet/0.7/) (link) instead of trying to create my own figlet in the 
`Start Screen` that says `F1 QUIZ`. 

![Screenshot of pyfiglet]()

I used the `sort()` method after suggested to do so by my mentor [Benjamin Kavanagh](https://github.com/BAK2K3) for sorting my leaderboard rankings, I found this method in the documentation for `GSPREAD`. It can be found [here](https://docs.gspread.org/en/latest/api.html?highlight=sort#gspread.worksheet.Worksheet.sort) (link). 

![Screenshot of sort() method GSPREAD docs]()

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
![Screenshot new repository button github]()
1. Select in the dropdown menu under `Repository template` if you for example would like to use the template provided by `Code Institute` that I did for this project. If you don't see it in the dropdown menu click this [link](https://github.com/Code-Institute-Org/python-essentials-template) to get to the one provided by `Code Institute` and click `Use this template` to the left of the green Gitpod button.
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

This instructions were taken from [Github - Fork a repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo). 

### Cloning GitHub Repository

Cloning a repository inolves making a full copy of a repository on your local machine. This allows you to work on the code easier. Changes can be pushed back up to the Github site or changes from other sources pulled to your local copy. I will explain how to clone down below: 

1. Go to the repository page on Github. 
1. Above the file list click on the green button that says `"Code"`. 
1. You can choose to download a zip file of the repository, to unpack it on your local machine and open it in your IDE. 
1. Clone using HTTPS by copying the URL under the HTTPS tab. 
1. Open a terminal window, set current directory to the one you want to contain the clone from. 
1. Type `git clone` and paste the URL copied from the Github page. 
1. The repository clone will now be created on your machine. 

This instructions were taken from [Github - cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

### Heroku 

Deploying a project using Heroku: 

* Visit the [Heroku](https://www.heroku.com) (link) website and click on create an account. 
* Click the `"New"` button. 
* Click the `"Create new app"` button. 
* Provide a name for the app in the `App` name input field. 
* Select your region from the `"choose region"` dropdown menu. 
* Click the `"Create App"` button. 
* Once redirected, proceed to the settings tab. 
* Click on the `"config vars"` button. 
* Supply a `KEY` of `PORT` and it's value of `8000`. Then click the `"add"` button. 
* Next step is to add `Buildpacks`, click the `"Add Buildpack"` button. 
* The `python` buildpack needs to be added first then the `node js` buildpack. 
* Once the buildpacks have completed, got to the deploy screen, once in the deploy screen, select GitHub as the deployment method and connect your GitHub profile. 
* Search for the repository that you wish to deploy to `Heroku` and click `"connect"`. 
* Once your repository is connected to Heroku you can choose to either automatically or manually deploy your app. 
* I choose manual deploy beacuse I like to refresh the branch myself when I update my project. 
* By selecting automatic deploy, Heroku will build a new version of the app each time a change has been made and pushed to the repository on `GitHub`. 
* By selecting manual deploys, it allows you to build a new version of your app whenever you click manual deploy. 
* If your build is successful you will then be able to visit the live site by clicking the link that is provided to you by `Heroku`. 

New way of deploy project to heroku: 
* When you want to deploy your project to `Heroku`. 
* Type `heroku login -i` to login to your existing account (if you have one) in the `Gitpod` terminal. 
* Then run the command `heroku create your_app_name_here` to create a new app (the name has to be uniqe). 
* Now you can see your new project at `Heroku` dashboard and set the config vars and buildpacks as the steps explained above. 

The command to add packages to the requirments.txt file, `pip3 freeze --local > requirments.txt`. 


---
## Support 

I would like to give an extra `Thank you` to all the kind people I have around me that gave me support in all different ways. 

* **Code Institute** for their **Tutor** support. 
* My mentor [Benjamin Kavanagh](https://github.com/BAK2K3) for being a **Superior** mentor.
* **Google** for always clear things up.
* My lovely **Girlfriend** for always supporting and believing in me.

### RETURN TO THE [TOP](#formula-one-quiz)
