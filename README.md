# Webmaster - Spring 2019
>2019 Kentucky Technology Student Assocition Webmaster High School Submission (1st Place)

For the 2019 KYTSA Webmaster High School competition, the challenge was to make a website for a band. The requirements included pages that gives info about songs, merchandise, 
concerts, and a blog where users can talk. Additionally, links to your school's websites are required. <br/><br/>
I built my website using Flask. As well as meeting the challenge requirements, I added additional quality of life features. 
Users can search for concerts, purchase tickets, purchase merchandise, and create an account for users to post blogs.
Purchases made are fake and only send email receipts from a mailing account. Blog posts and accounts are stored in a SQLite database.
*This app has been tested to work on desktop and mobile devices.*

This web app is currently deployed on https://webmaster-2019-renzjordan.onrender.com/ (as of Jan. 2023).
<br/>

## Features

* Concert Searching
* Ticket and Merch Purchasing
* Account System
  * Hashed Passwords
  * Unique email for each account
  * Ability to change email, username, and password
  * Profile pictures
* Blog System
  * User accounts can make blog posts that all users see
  * Can see all posts made by a user
  * Users can update or delete posts they've made
* Responsive Design
  
 

## Tech Stack

* Flask (Python)
* SQLite
* HTML, CSS