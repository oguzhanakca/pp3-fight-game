# **Arena**

Developed by Oğuzhan Akça

<img src="docs/am-i-responsive.jpg" alt="The screenshot of Am I Responsive">

[Live Site](https://arena-fight-977683a914a6.herokuapp.com/)

## Introduction

Arena is a Python terminal game, which runs in the Code Institute mock terminal on Heroku. It is a turn-based fighting game that challenges users with different types of enemies. The objective of the game is facing varius type of enemies and getting better equipment with the gold they earn from challenges. In order to beat the game, users have to challenge with the boss "Demon King".

Users must use their special attack at the right time to beat their enemies. Otherwise enemies will recover a huge part of their health.

Even users lose a fight, they can still keep playing. But they will lose a decent amount of gold as a penalty.

Users should create an account to be able to play. They can also use the account whenever they want without losing their progress. Every user can give once a feedback after they beat the game.

## Contents

- [Project Goals](#project-goals)<br>
  - [User Goals](#user-goals)
  - [Site Owner Goals](#site-owner-goals)
- [User Experience](#user-experience)<br>
  - [Target Audience](#target-audience)
  - [User Requirements](#user-requirements)
  - [User Stories](#user-stories)
  - [User Manual](#user-manual)
- [Technical Design](#technical-design)
  - [Data Models](#data-models)
  - [Flowchart](#flowchart)
- [Features](#features)
  - [App Features](#app-features)
  - [Feature Ideas for future development](#feature-ideas-for-future-development)
- [Technologies Used](#technologies-used)
- [Deployment & Local Development](#deployment--local-development)
- [Testing](#testing)
  - [Validation](#validation)
  - [Manual Testing](#manual-testing)
  - [Automated Testing](#automated-testing)
  - [Bugs](#bugs)
- [Credits](#credits)

## Project Goals

### User Goals

- Playing a challenging turn-based combat game.
- To be able to play again from where i stopped.

### Site Owner Goals

- Create a challenging game.
- To ensure users have a fun time.

## User Experience

### Target audience

- Users who like to play turn-based combat games
- Users who like to spend time on grinding.

### User requirements

- A game that is understandable and works as expected.
- Log-in and sign up works as expected.
- Users can quit the game whenever they want.
- Even if users leave the game, they can keep their progress and continue from where they left.

### User Stories

#### As a new user,

1. I want to create an account.
2. I want to read the guide.
3. I want to leave feedback.
4. I want to see my stats.
5. I want to see how much gold i have.
6. I want to easily navigate within the game.

#### As a returning user,

7. I want to login to my account.
8. I want to remember how to play.
9. I want to leave feedback.
10. I want ot see my stats.
11. I want to see how much gold i have.
12. I want to easily navigate within the game.

#### As the site owner,

13. I want users to create an account.
14. I want users to log in the existing account.
15. I want users to learn how to play.
16. I want users to easily navigate within the game.
17. I want users to see their current stats.
18. I want users to see the current gold they have.
19. I want users to be able to give feedback.

### User Manual

<details>
<summary>View Manual</summary>

### Start Menu

When the program starts, the user will be asked whether to log in or register.

- Users will be navigated by their prompt
- Every input will be validated whether its invalid input or not.

### Log in

The program will ask user to type their username and password. To login successfully:

- Username will be checked whether it exists in database or not.
- Password will be checked whether its correct or not.
- Process can be aborted with "x" input.

### Register

The program will ask user to type their desired username(which will be the name of user's character) and password. To register successfully:

- Username must be between 5 and 15 characters long.
- Username must only contain alphabetic characters.
- Username must not contain any spaces.
- Username must not already exist.
- Password must be between 5 and 15 characters long.
- Password must not contain any spaces.
- Process can be aborted with "x" input.

PS :
Passwords are case sensitive. Usernames are not.

### Main menu

After successfully logged in, the user will be navigated to main menu. Here users will see the options:

1. Visit Shop
2. Enter Arena
3. Stats
4. How to play
5. Quit game

Users can navigate through by the numbers every option has.

### Shop

It will display after the player chooses to visit shop. The user will have 3 options:

1. Weapon Shop
2. Armor Shop
3. Leave Shop

If the user chooses the 3rd option, they will be navigated back to main menu.
If the user chooses anything else than leaving shop, they will be navigated to the shop they choosed.

### Weapon and Armor shop

Every shop will load their own content from the database. If the users have enough gold, they can buy their equipment here.

- When the user tries to buy something that is worse or equal to their current equipment, they will be asked if they still want to do it or not.

### Enter Arena

It will display the enemies user can face and leave arena option. Every enemy will drop some amount of gold that user can use to upgrade their equipment.

- It is recommended to kill enemies with the order they listed.
- Users should try to upgrade their equipment to face stronger enemies.
- Users will lose decent amount of gold if they lose a fight.

### Stats

It will show current stats of the user with the weapon and armor included.

### How to play

It will display a guide to the users. Users can press 1 to return to main menu.

### Combat

When users decides to face an enemy, combat system will appear. Every round users will be asked which action they want to do:

1. Attack
2. Special Attack
3. Run Away

- Attack option deals damage to the enemy equal to the player's damage.
- Special attack option deals 2x damage the user will do. Also stuns enemy in that round. Users can block enemies recover skill with special attack.
- Special attack has a cooldown. To activate it again, user must land a successful normal attack.
- Everyone can deal critical damage which is 2x of their damage. If special attack deals critical damage, it will deal 4x of user's damage.
- Armors reduce attacker's damage.
- Everyone can dodge attacks depending on their evasion stat
- User can attempt to run away from the fight. It has 25% success rate. If user fails to run away, they will skip their turn.

### Completing the game

To beat the game, user must defeat the Demon King, which will be showed in Arena Menu.

### Feedback

The user will be asked once they finish the game to give feedback.

- Every account can give only one feedback.
- If users didn't give an feedback once they clear the game, they can kill the Demon King again and give feedback.

</details><br>

## Technical Design

### Flowchart

The flowchart created by using [Lucidchart](https://lucid.app/) to visualise the logic flow of the game.

<details>
    <summary>Flowchart</summary>
    <img src="docs/technical-design/flowchart.jpg" alt="The screenshot of flowchart">
</details><br>

### Data Models

I decided to eight classes in this project. The classes used in this project are:

1. Player : Holds the data of logged user.
2. Stats : Calculates the stats of user included weapon and armor
3. Weapon : Holds the current weapon data of the user
4. Armor : Holds the current armor data of the user
5. Enemy : Holds the data of the enemy that has chosen in arena
6. PlayerCombat : Holds the data of user in combat
7. EnemyCombat : Holds the data of enemy in combat
8. Combat : The class that has methods to perform the fight
   - The combat class also has methods to handle the combat for enemy and user side.

- The Google Sheets API was used for keeping user data, weapon, armor, enemy and user feedback submissions.
  - This allows users to keep their progress even when they exit the game.

## Features

The website has a single page with several features within the mock python terminal. These features are listed below.

- Each feature has its own validation against user input.

### Start Screen

It will be shown when user start the program.

- Displays the name of program
- Asks users whether they want to register or login
- User stories covered:

![Start Screen](docs/features/start-screen.jpg)

### Login

Shown when the user selects the login option

- Prompts users for their username and password
- Usernames are not case sensitive.
- Passwords are case sensitive.
- Validates if username exists and password is correct.
- User stories covered:

![Login](docs/features/login.jpg)

### Register

Shown when the user selects the register option

- Prompts users for their desired username and password
- Usernames are not case sensitive.
- Passwords are case sensitive.
- Validates if username exists or in correct format.
- Validates if password is in correct format.
- User stories covered:

![Register](docs/features/register.jpg)

### Main Menu

Shown after successful login. The main navigation menu of the game.

- Displays user's name.
- Asks users what they want to do.
- Validates against wrong input.
- User stories covered:

![Main Menu](docs/features/main-menu.jpg)

### Shops

Shown after the user selects Visit Shop option

- Allows users to improve their equipment
- Displays the stats and prices of the items.
- Each shop validates whether user has enough gold or not.
- Each shop validates whether the desired equipment is equal or better than current equipment.
- Users can navigate back to main menu.
- Validates against wrong input.
- User stories covered:

![Shop Menu](docs/features/shop-menu.jpg)
![Shops](docs/features/shops.jpg)

### Arena

Shown after the user selects Enter Arena option

- Allows users to choose which enemy they want to face.
- Users can navigate back to main menu.
- Validates against wrong input.
- User stories covered:

![Arena Menu](docs/features/arena-menu.jpg)

### Stats

Shown after the user selects Stats option

- Displays user's currently equipped weapon and armor.
- Displays user's current stats.
- Users can navigate back to main menu.
- Validates against wrong input.
- User stories covered:

![Stats](docs/features/stats.jpg)

### How to Play

Shown after the user selects How to Play option.

- It shows the guide related to the game.
- Users can also find some tips about the game.
- Users can navigate back to main menu.
- Validates against wrong input.
- User stories covered:

![Guide](docs/features/guide.jpg)

### Combat

Shown after the user selects an enemy from Arena.

- Displays current/max health of both user and enemy.
- Displays current round.
- Gives users three action options.
- After the user's decision, simulates the fight.
- If users choose "run away" option, they can navigate back to main menu.(This option has 25% chance to success.)
- Automatically navigates to main menu after the fight ends.
- Validates against wrong input.
- User stories covered:

![Combat](docs/features/start-screen.jpg)

### Feedback

Shown after the user finished the game.

- Asks users if they want to give a feedback.
- Each account can only provide one feedback.
- No matter what the choice is, it exists the game after the selection.
- Validates against empty input.
- User stories covered:

![Start Screen](docs/features/start-screen.jpg)

### Feature ideas for future development

- Various types of enemies can be added.
- Various types of actions, skills can be added.
- Various types of items can be added.
- Quest system can be added.

## Technologies Used

### Languages used

Python

### Other Tools

- [Lucidchart](https://lucid.app/) was used to create flowchart.
- [Git](https://git-scm.com/) was used for version control.
- [GitHub](https://github.com/) was used for saving and storing files.
- [Heroku](https://id.heroku.com/) was used as the hosting platform for this site.
- [Ascii art generator](http://patorjk.com/software/taag/#p=display&f=Varsity&t=Dungeon%0AEscape) was used to generate title text.
- [amiresponsive](https://ui.dev/amiresponsive?url=https://jeremyhsimons.github.io/CI_PP2_SavvySaver/) was used to test the website across different screens.

#### 3rd party Python Libraries used

- [Gspread / Google Sheets API](https://github.com/burnash/gspread)
- [Google OAuth 2.0](https://google-auth.readthedocs.io/en/stable/reference/google.oauth2.credentials.html)
- [Colorama](https://pypi.org/project/colorama/)
- [OS](https://docs.python.org/3/library/os.html)

## Deployment & Local Development

The website was deployed to [Heroku](https://id.heroku.com/) using the following process:

1. Login or create an account at [Heroku](https://dashboard.heroku.com/)
   <img src="docs/heroku/heroku1.png">
1. Click on New > Create new app in the top right of the screen.
   <img src="docs/heroku/heroku2.png">
1. Add an app name and select location, then click 'create app'.
   <img src="docs/heroku/heroku3.png">
1. Under the deploy tab of the next page, select connect to GitHub.
1. Log in to your GitHub account when prompted.
   <img src="docs/heroku/heroku4.png">
1. Select the repository that you want to be connected to the Heroku app.
   <img src="docs/heroku/heroku5.png">
1. Click on the settings tab.
   <img src="docs/heroku/heroku6.png">
1. Scroll down to the config vars section, and add 2 config vars:
   _ The first key is CREDS and the value here is the creds.json file that was generated for the google sheets API to work properly.
   _ The second key is PORT and the Value is 8000
   <img src="docs/heroku/heroku7.png">
1. Once you have set up the config vars, scroll down to buildpacks (still under the settings tab)
1. Add the Python and Node.js buildpacks to your app and make sure that when they are displayed, they appear in the order:
   _ Python
   _ Node.JS
   <img src="docs/heroku/heroku8.png">
1. Navigate back to the settings tab.
1. Select automatic deploys to allow Heroku to build the site with new changes each time changes are pushed to GitHub.
   <img src="docs/heroku/heroku9.png">
1. In the 'manual deploy' section beneath this, make sure the branch selected is 'main' and click deploy branch.
   <img src="docs/heroku/heroku10.png">
1. The site should now be built and Heroku should provide a url for the built site.

This repository can be forked using the following process:

1. On the repository's page, go to the top-right of the page underneath the dark ribbon.
1. Click on the fork button
1. You can now work on a fork of this project.

This repository can be cloned using the following process:

1. Go to this repository's page on GitHub.
1. Click on the code button (not the one in the navbar, but the one right above the file list).
1. Select an option, HTTPS, SSH, GitHub CLI.
1. Copy the url below to your clipboard.
1. Open Git Bash/your IDE terminal.
1. Ensure the directory you are working in is the correct one you want to paste the project into.
1. Type the command '$ git clone'
1. Paste the URL of the repository after this.
1. Hit enter on your keyboard and the project will be cloned.

## Testing

### Debugging

The site was tested using the following browsers:

- Google Chrome
- Opera
- Microsoft Edge

The site was tested on the following devices:

- Iphone 6S
- Huawei PSmart 2019 (EMUI version 12.0.0)

### Validation

#### PEP8 Python Validator (from Code Institute)

Code institute's own Python Linter [pep8](https://pep8ci.herokuapp.com/) was used to validate all Python code in this project.

Errors found by the validator:

- W291 trailing whitespace
- W605 invalid escape sequence
- E501 line too long
- E302 expected 2 blank lines

All errors found by the validator have been fixed.

<details>
<summary>instructions.py</summary>
<img src="docs/validation/instructions-v.png" alt="A screenshot of pep8 validator confirming instructions code.">
</details>

<details>
<summary>run_game.py</summary>
<img src="docs/validation/run_game-v" alt="A screenshot of pep8 validator confirming game code.">
</details>

<details>
<summary>run.py</summary>
<img src="docs/validation/run-v.png" alt="A screenshot of pep8 validator confirming main program code.">
</details>

<details>
<summary>sheet_data.py</summary>
<img src="docs/validation/sheet_data-v.png" alt="A screenshot of pep8 validator confirming sheet API code.">
</details>

<details>
<summary>test_validation.py</summary>
<img src="docs/validation/test_validation-v.png" alt="A screenshot of pep8 validator confirming testing code.">
</details>

<details>
<summary>validation.py</summary>
<img src="docs/validation/validation-v.png" alt="A screenshot of pep8 validator confirming validation code.">
</details>
<br>

### Manual Testing

| User story                 | Feature        | Test                                                                                          | Expected Result                | Actual Result      |
| -------------------------- | -------------- | --------------------------------------------------------------------------------------------- | ------------------------------ | ------------------ |
| 1. Sign up as a new player | Sign-up prompt | When prompted by the opening view of the game, answer 'n', enter new details and type 'enter' | Program accepts/signs user up. | Works as expected. |

<details>
    <summary>Screenshots</summary>
    <img src="docs/manualtest/us1-1.png" alt="A screenshot of the sign up prompt."><br>
    <img src="docs/manualtest/us1-2.png" alt="A screenshot of the sign up prompt."><br>
    <img src="docs/manualtest/us1-3.png" alt="A screenshot of the new users details."><br>
    <img src="docs/manualtest/us1-4.png" alt="A screenshot of the success notification."><br>
    <img src="docs/manualtest/us1-5.png" alt="A screenshot of the new user stored in google sheets."><br>
</details><br>

| User story                            | Feature   | Test                                                     | Expected Result                                                  | Actual Result      |
| ------------------------------------- | --------- | -------------------------------------------------------- | ---------------------------------------------------------------- | ------------------ |
| 2. Instructions before starting game. | Main menu | When in the main menu, enter 'i' to access instructions. | Program displays instructions and a way to get back to the menu. | Works as expected. |

<details>
    <summary>Screenshots</summary>
    <img src="docs/manualtest/us2-1.png" alt="A screenshot of the main menu."><br>
    <img src="docs/manualtest/us2-2.png" alt="A screenshot of the instructions."><br>
</details><br>

| User story                           | Feature    | Test                                                            | Expected Result                                                                     | Actual Result      |
| ------------------------------------ | ---------- | --------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ------------------ |
| 3. Visual representation of the game | Level view | When user starts the game, a view of the level appears clearly. | Program displays level, which is updated with each successful move the player makes | Works as expected. |

<details>
    <summary>Screenshots</summary>
    <img src="readme-docs/testing-user-stories/us3-1.png" alt="A screenshot of the main menu with s selected."><br>
    <img src="readme-docs/testing-user-stories/us3-2.png" alt="A screenshot of a new game"><br>
</details><br>

| User story                                           | Feature        | Test                                                            | Expected Result                              | Actual Result      |
| ---------------------------------------------------- | -------------- | --------------------------------------------------------------- | -------------------------------------------- | ------------------ |
| 4. Erroneous data entry to be caught by the program. | Sign up prompt | When at the starting view, enter a response that is not y or n. | Program flags this as an incorrect response. | Works as expected. |

<details>
    <summary>Screenshots</summary>
    <img src="docs/manualtest/us4-1.png" alt="A screenshot of the sign up prompt with invalid entry."><br>
    <img src="docs/manualtest/us4-2.png" alt="A screenshot of the error message."><br>
</details><br>

| User story                                            | Feature        | Test                                                                       | Expected Result                                                                          | Actual Result      |
| ----------------------------------------------------- | -------------- | -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ------------------ |
| 5. Player mistakes/wrong answers to receive feedback. | Maths question | When presented with a maths question, deliberately enter the wrong answer. | Program flags this as an incorrect answer and tells the user that they have lost a life. | Works as expected. |

<details>
    <summary>Screenshots</summary>
    <img src="docs/manualtest/us5.png" alt="A screenshot of a maths question with wrong answer and program's feedback."><br>
</details><br>

| User story                                 | Feature       | Test              | Expected Result                                                        | Actual Result      |
| ------------------------------------------ | ------------- | ----------------- | ---------------------------------------------------------------------- | ------------------ |
| 6. Receive a score at the end of the game. | End game view | Complete the game | Program notifies user of their score and saves it to the google sheet. | Works as expected. |

<details>
    <summary>Screenshots</summary>
    <img src="docs/manualtest/us6.png" alt="A screenshot of the end game page."><br>
</details><br>

| User story                    | Feature        | Test                                                                           | Expected Result                                         | Actual Result      |
| ----------------------------- | -------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------- | ------------------ |
| 7. Log into existing account. | Sign up prompt | When prompted, answer yes to existing account and log in with existing details | Program checks user and lets them access the game menu. | Works as expected. |

<details>
    <summary>Screenshots</summary>
    <img src="docs/manualtest/us7-1.png" alt="A screenshot of existing user logging in."><br>
    <img src="docs/manualtest/us7-2.png" alt="A screenshot of welcome message"><br>
</details><br>

| User story            | Feature   | Test                                                       | Expected Result                                         | Actual Result      |
| --------------------- | --------- | ---------------------------------------------------------- | ------------------------------------------------------- | ------------------ |
| 8. Skip instructions. | Main menu | When in main menu, enter 's' to start the game immediately | Program loads the game when this response is submitted. | Works as expected. |

<details>
    <summary>Screenshots</summary>
    <img src="docs/manualtest/us8-1.png" alt="A screenshot of the main menu"><br>
    <img src="docs/manualtest/us8-2.png" alt="A screenshot of a new game."><br>
</details><br>

| User story                            | Feature    | Test                                      | Expected Result                                                                                        | Actual Result      |
| ------------------------------------- | ---------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------ |
| 9. Play a different game than before. | Level view | Start the game and complete a few levels. | Program has re-organised levels into a different order than before, and maths questions are different. | Works as expected. |

<details>
    <summary>Screenshots</summary>
    <img src="docs/manualtest/us9-1.png" alt="A screenshot of a new level 1."><br>
    <img src="docs/manualtest/us9-2.png" alt="A screenshot of a different randomised level 1."><br>
</details><br>

| User story         | Feature     | Test                                                                                         | Expected Result                            | Actual Result      |
| ------------------ | ----------- | -------------------------------------------------------------------------------------------- | ------------------------------------------ | ------------------ |
| 10. Send feedback. | Quit screen | When prompted, answer yes to giving feedback and type a message. Then press enter to submit. | Program sends message to the google sheet. | Works as expected. |

<details>
    <summary>Screenshots</summary>
    <img src="docs/manualtest/us10-1.png" alt="A screenshot of a new feedback message from user."><br>
    <img src="docs/manualtest/us10-2.png" alt="A screenshot of program's response."><br>
    <img src="docs/manualtest/us10-3.png" alt="A screenshot of the feedback saved in google sheets."><br>
</details><br>

| User story                                 | Feature        | Test                                          | Expected Result                               | Actual Result                                 |
| ------------------------------------------ | -------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| 11. (Site owner) Ensure data is validated. | Sign up prompt | Same test as user story 4. See details above. | Same test as user story 4. See details above. | Same test as user story 4. See details above. |

| User story                                               | Feature        | Test                                          | Expected Result                               | Actual Result                                 |
| -------------------------------------------------------- | -------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| 12. (Site owner) Ensure user actions are given feedback. | Maths question | Same test as user story 5. See details above. | Same test as user story 5. See details above. | Same test as user story 5. See details above. |

| User story                                       | Feature        | Test                         | Expected Result                                                                        | Actual Result      |
| ------------------------------------------------ | -------------- | ---------------------------- | -------------------------------------------------------------------------------------- | ------------------ |
| 13. (Site owner) Test user's arithmetic ability. | Maths question | Complete a level in the game | To be presented with a multiplication question with 2 random numbers between 5 and 20. | Works as expected. |

<details>
    <summary>Screenshots</summary>
    <img src="docs/manualtest/us13-1.png" alt="A screenshot of level 1 being completed"><br>
    <img src="docs/manualtest/us13-2.png" alt="A screenshot of level complete screen."><br>
    <img src="docs/manualtest/us13-3.png" alt="A screenshot of a new maths question after level complete."><br>
</details><br>

| User story                                   | Feature     | Test                                           | Expected Result                                | Actual Result                                  |
| -------------------------------------------- | ----------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| 14. (Site owner) To get feedback from users. | Quit screen | Same test as user story 10. See details above. | Same test as user story 10. See details above. | Same test as user story 10. See details above. |

### Automated Testing

Seven unit tests were written for this project. The test check that the validation functions (used to check user inputs) return the expected results.

Most tests originally failed because error handling to catch invalid data types had not been included. Once this had been addressed, all tests passed OK.

For each unit test, the assertions test:

- Valid data
- Invalid data and edge cases.

<details>
    <summary>Screenshots</summary>
    <p>All tests passed OK.</p>
    <img src="docs/unittests/tests-passed.png" alt="A screenshot of the Gitpod terminal stating that all tests have passed.">
    <p>1. Test validate_yes_no</p>
    <img src="docs/unittests/test1.png" alt="A screenshot of the first test">
    <p>2. Test validate_details</p>
    <img src="docs/unittests/test2.png" alt="A screenshot of the second test">
    <p>3. Test validate_main_menu</p>
    <img src="docs/unittests/test3.png" alt="A screenshot of the third test">
    <p>4. Test validate_math</p>
    <img src="docs/unittests/test4.png" alt="A screenshot of the fourth test">
    <p>5. Test validate_navigation</p>
    <img src="docs/unittests/test5.png" alt="A screenshot of the fifth test">
    <p>6. Test validate_string</p>
    <img src="docs/unittests/test6.png" alt="A screenshot of the sixth test">
    <p>7. Test validate_message</p>
    <p>This test originally failed because checks for empty strings or spaces had been omitted. Once this had been added to the validation function, the test passed.</p>
    <img src="docs/unittests/test7.png" alt="A screenshot of the seventh test">
</details><br>

### Bugs

| Bug Description                                                                                                                                                   | Action Taken to Fix                                                                                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The user could sign up with empty username/password fields                                                                                                        | I added condition to the validation function that catches empty strings.                                                                                                                                              |
| Submitting user’s feedback would throw an error in the terminal                                                                                                   | I had forgotten to format the feedback data as a list, and I was trying to update the sheet with a string. Making a single element list out of the feedback before sending it to the update function fixed the issue. |
| Index error each time the levels were generated.                                                                                                                  | The list used to randomly order layouts was numbered 1-10 where layouts are indexed 0-9. Changing random order list to integers between 0 and 9 fixed this.                                                           |
| When player makes a mistake and navigates into a wall, the notification gets printed twice to the terminal.                                                       | Change each check direction function so that it only calls the check route function once.                                                                                                                             |
| When player makes invalid menu choice, “start” selection doesn’t work on second try and script stops.                                                             | I put the menu in a while loop rather than re-calling the function with the same parameters in an if-else statement.                                                                                                  |
| When player moved out of bounds, the level would not reset to the original layout, and the updated level with all progress so far was re-printed to the terminal. | A separate reset function was created to loop through the level elements and reset the “A” character to the start.                                                                                                    |
| If player selected “no” to whether they wanted to quit, the game still quit.                                                                                      | I added the missing if else statement that I’d forgotten to include to handle that choice.                                                                                                                            |

## Credits

### 3rd party code used

#### 3rd party Python libraries/modules

- [Gspread / Google Sheets API](https://github.com/burnash/gspread) was used to handle getting/sending data to the google sheet used in the project.
- [Google OAuth 2.0](https://google-auth.readthedocs.io/en/stable/reference/google.oauth2.credentials.html) was used to set up the connection between the project and the developers personal google account.
- [Colorama](https://pypi.org/project/colorama/) was used to add colour to the game for increased visual appeal.
- [Ascii art generator](http://patorjk.com/software/taag/#p=display&f=Varsity&t=Dungeon%0AEscape) was used to generate title text. Varsity font was used.

#### Code found online when solving bugs in own code.

- How to clear screen in python: [www.scaler.com](https://www.scaler.com/topics/how-to-clear-screen-in-python/)

- How to create unit tests in Python [Corey Schafer](https://www.youtube.com/watch?v=6tNS--WetLI)

### Acknowledgements

- Thanks to my Mentor Mo Shami for his <strong>immensely valuable</strong> feedback, advice and encouragement throughout this project. Thanks for pushing me to do the best I can!
- Thanks to the wonderful CI London Community for all the moral support!
- Thanks to my friends: Thommy, Lars, Matt, Nesu, Nathan, Rob, and Oli for testing the game and for their feedback.
