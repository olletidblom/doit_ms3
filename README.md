# DoIt - Django To-Do App

![Am I Responsive](docs/images/amiresponsive/amiresponsive.png)

**Developer: Olle
💻 [Visit Live Website](https://doitms3-10b442815bf1.herokuapp.com/)  
(Ctrl + click to open in new tab)

---

## 📖 Table of Contents
- [About](#about)
- [User Goals](#user-goals)
- [Site Owner Goals](#site-owner-goals)
- [User Experience](#user-experience)
- [User Stories](#user-stories)
- [Design](#design)
  - [Colours](#colours)
  - [Fonts](#fonts)
  - [Structure](#structure)
  - [Wireframes](#wireframes)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Validation](#validation)
- [Testing](#testing)
- [Bugs](#bugs)
- [Heroku Deployment](#heroku-deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

---

## 📝 About

DoIt is a simple and intuitive to-do list application built with Django. Users can create, edit, and delete tasks, making it easier to stay organized.

---

## 🎯 User Goals
- Create and manage tasks efficiently.
- Mark tasks as completed.
- Edit or delete tasks when needed.
- Responsive design for accessibility on any device.

## 🎯 Site Owner Goals
- Provide a simple and user-friendly task management system.
- Ensure security through authentication.
- Deploy a reliable and scalable web application.

---

## 🎨 User Experience

### 🎯 Target Audience
- Individuals looking for a simple task management solution.
- Professionals managing daily work tasks.
- Students organizing their assignments.

### 🎯 User Requirements & Expectations
- Simple and intuitive navigation.
- Fast task creation and management.
- Secure authentication.
- Mobile-friendly and responsive UI.

---

## ✅ User Stories

### Users
### Users
<details><summary>1. As a user, I can create a task so that I can track my to-dos.</summary>
<img src="docs/images/user_storys/1.png">
</details>

<details><summary>2. As a user, I can edit a task so that I can update its details.</summary>
<img src="docs/images/user_storys/2.png">
</details>

<details><summary>3. As a user, I can delete a task so that I can remove unnecessary tasks.</summary>
<img src="docs/images/user_storys/3.png">
</details>

<details><summary>4. As a user, I can mark a task as completed so that I can keep track of finished work.</summary>
<img src="docs/images/user_storys/4.png">
</details>

<details><summary>5. As a user, I can register and log in so that my tasks are saved.</summary>
<img src="docs/images/user_storys/5.png">
</details>

<details><summary>6. As a user, I can create and assign a category to a task.</summary>
<img src="docs/images/user_storys/6.png">
</details>

<details><summary>7. As a user, I can paginate through my task list so that I can navigate large lists easily.</summary>
<img src="docs/images/user_storys/7.png">
</details>

<details><summary>8. As a user, I can receive confirmation messages when I create, edit, or delete a task so that I know my actions were successful.</summary>
<img src="docs/images/user_storys/8.png">
</details>

<details><summary>9. As a user, I can log out so that my account remains secure.</summary>
<img src="docs/images/user_storys/9.png">
</details>

### Admin

<details><summary>10. As an admin, I can view all user tasks so that I can manage user activity.</summary>
<img src="docs/images/user_storys/10.png">
</details>

<details><summary>11. As an admin, I can delete inappropriate or spam tasks so that the platform remains clean.</summary>
<img src="docs/images/user_storys/11.png">
</details>

<details><summary>12. As an admin, I can create and manage categories so that users have a structured way to organize tasks.</summary>
<img src="docs/images/user_storys/12.png">
</details>

<details><summary>13. As an admin, I can enable or disable user accounts so that I can control platform access.</summary>
<img src="docs/images/user_storys/13.png">
</details>

<details><summary>14. As an admin, I can edit user tasks in case of data corrections or issues.</summary>
<img src="docs/images/user_storys/14.png">
</details>

<details><summary>15. As an admin, I can access an admin dashboard so that I can manage tasks and users efficiently.</summary>
<img src="docs/images/user_storys/15.png">
</details>

---

## 🎨 Design

### 🎨 Colours
A modern minimalistic colour scheme was used to keep the UI clean and easy to read.

### 🎨 Fonts
Georiga was used to ensure a professional and legible typeface.

### 🎨 Structure
The site follows a **dashboard-style layout**, with an intuitive **task management interface**.

# Database

- Built with Python and the Django framework using PostgreSQL for production (Heroku deployment).
- The database consists of three main models: `User`, `Category`, `Task`, and `Profile`.

<details><summary>Show diagram</summary>
<img src="docs/images/todoerd.png">
</details>

---

## User Model
The `User` model (from Django's built-in authentication system) contains the following fields:

- `id`
- `password`
- `last_login`
- `is_superuser`
- `username`
- `first_name`
- `last_name`
- `email`
- `is_staff`
- `is_active`
- `date_joined`

---

## Category Model
The `Category` model represents task categories and contains:

- `id` (Primary Key)
- `name` (CharField, max length: 100)
- `user` (ForeignKey to `User`, `CASCADE` on delete)

**Meta Constraints:**
- Unique constraint on `name` per `user`.

---

## Task Model
The `Task` model represents individual tasks and contains:

- `id` (Primary Key)
- `user` (ForeignKey to `User`, `CASCADE` on delete, related name: `tasks`)
- `title` (CharField, max length: 255)
- `description` (TextField, nullable)
- `completed` (BooleanField, default: `False`)
- `created_at` (DateTimeField, auto_now_add=True)
- `updated_at` (DateTimeField, auto_now=True)
- `category` (ForeignKey to `Category`, `SET_NULL` on delete, nullable, related name: `tasks`)

---

## Profile Model
The `Profile` model stores additional user details and contains:

- `id` (Primary Key)
- `user` (OneToOneField to `User`, `CASCADE` on delete)
- `fname` (CharField, max length: 50, nullable)
- `lname` (CharField, max length: 50, nullable)
- `bio` (RichTextField, max length: 300, nullable)
- `location` (CharField, max length: 100, nullable)
- `birthdate` (DateField, nullable)
- `updated_at` (DateTimeField, default: `timezone.now`)

### Signals:
A `post_save` signal is used to automatically create a `Profile` for each new `User` instance.

```python
@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
```

### 🎨 Wireframes
Wireframes were created using [Balsamiq](https://balsamiq.com/) to plan the UI structure.

<details><summary>Log In</summary>
<img src="docs/images/wireframes/login.png">
</details>
<details><summary>Sign Up</summary>
<img src="docs/images/wireframes/signup.png">
</details>
<details><summary>Task List</summary>
<img src="docs/images/wireframes/todolist.png">
</details>
<details><summary>Task View</summary>
<img src="docs/images/wireframes/todoview.png">
</details>
<details><summary>User Info</summary>
<img src="docs/images/wireframes/userinfo.png">
</details>

---

## 🛠️ Technologies Used

### 📌 Languages & Frameworks
- **Python** (Django Framework)
- **HTML, CSS** (Bootstrap 5 for styling)
- **JavaScript** (for interactive UI elements)
- **PostgreSQL** (Database)

### 📌 Libraries & Tools
- **Django-Allauth** (User authentication)
- **WhiteNoise** (Static file handling on Heroku)
- **Crispy Forms** (Bootstrap styling for forms)
- **djrichtextfield** (Rich text formatting)
- **Heroku** (Deployment)
- **GitHub** (Version control)

---
## Features

### Log In
- If user isn't logged in, this will be the first screen people see
- Links to signup
- Clean and easy interface


<details><summary>See feature images</summary>

![Log In](docs/images/features/login.png)
</details>


### Navigation
- Name of the app
- Fully Responsive
- On small screens switches to hamburger menu
- Indicates login/logout in status
- Displayed on all pages

<details><summary>See feature images</summary>

![Navigation](docs/images/features/navbar.png)
</details>


### Footer
- Shows logged in as: {{user}} if logged in.
- Log out
- Displayed across all pages
- Sign in if not logged in

<details><summary>See feature images</summary>

![Footer](docs/features/feature-footer.PNG)
</details>


### Sign Up
- Allow users to register an acoount


<details><summary>See feature images</summary>

![Sign up](docs/features/feature-register.PNG)
</details>


### Tasklist
- Shows users tasks
- Paginated by 5
- Allows user to create, edit and delete tasks

<details><summary>See feature images</summary>

![Tasklist](docs/images/features/tasklist.png)
![Login](docs/features/feature-login2.PNG)
</details>


### Logout
- Allows the user to securely log out
- Ask user if they are sure they want to log out

<details><summary>See feature images</summary>

![Logout](docs/images/features/logout.png)
</details>


### Category
- Allows the user to create, edit and delete categorys

<details><summary>See feature images</summary>

![Book](docs/features/feature-book-table.PNG)
![Categorys](docs/images/features/categorys.png)
</details>


### Account
- Allows the user to see and edit their user profile

<details><summary>See feature images</summary>

![My Bookings](docs/images/features/account.png)
</details>

### Messages
- Allows the user to see what they done

<details><summary>See feature images</summary>

![My Bookings](docs/images/features/message.png)
</details>

##### Back to [top](#table-of-contents)<hr>


---


## ✔️ Validation

- HTML and CSS validated using **W3C Validator**.
- Python code checked with **PEP8 compliance**.
- JavaScript validated using **JSHint**.
- Accessibility tested using **Lighthouse** and **WAVE**.

### HTML Validation
The W3C Markup Validation Service was used to validate the HTML of the website. All pages pass with no errors but some warnings to show.
<details><summary>Tasklist</summary>
<img src="docs/images/validation/html/tasklist.png">
</details>
<details><summary>TaskCrud</summary>
<img src="docs/images/validation/html/edittask.png">
<img src="docs/images/validation/html/creattask.png">
<img src="docs/images/validation/html/deletetask.png">
</details>
<details><summary>Categorylist</summary>
<img src="docs/images/validation/html/category.png">
</details>
<details><summary>CategoryCrud</summary>
<img src="docs/images/validation/html/editcategory.png">
<img src="docs/images/validation/html/createcategory.png">
<img src="docs/images/validation/html/deletecategory.png">
</details>
<details><summary>Profilee</summary>
<img src="docs/images/validation/html/profile.png">
</details>
<details><summary>Login, Signup, Logout</summary>
<img src="docs/images/validation/html/login.png">
<img src="docs/images/validation/html/signup.png">
<img src="docs/images/validation/html/logout.png">
</details>


### CSS Validation
The W3C Jigsaw CSS Validation Service was used to validate the CSS of the website.
The style.css file was approved.
<details><summary>style.css</summary>
<img src="docs/images/validation/css/css.png">
</details>

### JavaScript Validation
JSHint JS Validation Service

<details><summary>Script.js</summary>
<img src="docs/images/validation/js/js.png">
</details><hr>

### PEP8 Validation
Python code checked with **PEP8 compliance**


### Accessibility
The WAVE WebAIM web accessibility evaluation tool was used to ensure the website met high accessibility standards. All pages pass with 0 errors.
<details><summary>Tasklist</summary>
<img src="docs/images/validation/accessibillity//tasklist.png">
</details>
<details><summary>TaskCrud</summary>
<img src="docs/images/validation/accessibillity/edittask.png">
<img src="docs/images/validation/accessibillity/createtask.png">
<img src="docs/images/validation/accessibillity/deletetask.png">
</details>
<details><summary>Categorylist</summary>
<img src="docs/images/validation/accessibillity/categorys.png">
</details>
<details><summary>CategoryCrud</summary>
<img src="docs/images/validation/accessibillity/editcategory.png">
<img src="docs/images/validation/accessibillity/createcategory.png">
<img src="docs/images/validation/accessibillity/deletecategory.png">
</details>
<details><summary>Profilee</summary>
<img src="docs/images/validation/accessibillity/profile.png">
</details>
<details><summary>Login, Signup, Logout</summary>
<img src="docs/images/validation/accessibillity/login.png">
<img src="docs/images/validation/accessibillity/signup.png">
<img src="docs/images/validation/accessibillity/logout.png">
</details>

### Performance 
Google Lighthouse in Google Chrome Developer Tools was used to test the performance of the website. 

<details><summary>Tasklist</summary>
<img src="docs/images/validation/lighthouse/tasklist.png">
</details>
<details><summary>TaskCrud</summary>
<img src="docs/images/validatio/lighthouse/edittask.png">
<img src="docs/images/validation/lighthouse/createtask.png">
<img src="docs/images/validation/lighthouse/deletetask.png">
</details>
<details><summary>Categorylist</summary>
<img src="docs/images/validation/lighthouse/categorys.png">
</details>
<details><summary>CategoryCrud</summary>
<img src="docs/images/validation/lighthouse/editcategory.png">
<img src="docs/images/validation/lighthouse/createcategory.png">
<img src="docs/images/validation/lighthouse/deletecategory.png">
</details>
<details><summary>Profilee</summary>
<img src="docs/images/validation/lighthouse//profile.png">
</details>
<details><summary>Login, Signup, Logout</summary>
<img src="docs/images/validation/lighthouse/login.png">
<img src="docs/images/validation/lighthouse/signup.png">
<img src="docs/images/validation/lighthouse/logout.png">
</details>


---

## 🧪 Testing

### ✅ Manual Testing
- Tested on multiple browsers (Chrome, Firefox, Safari).
- Mobile responsiveness verified on real devices and emulators.

---

## 🐞 Bugs

### Fixed Issues
- **CSS not loading on Heroku** → Fixed by setting `STATIC_ROOT` and using WhiteNoise.
- **Missing environment variables** → Resolved by setting `SECRET_KEY` and `DATABASE_URL` in Heroku.

### Known Issues
- Some minor UI inconsistencies on smaller screens.

---

## 🚀 Heroku Deployment

### 1️⃣ **Create Heroku App**
```sh
heroku create doit-todo-app
```

### 2️⃣ **Set Up Environment Variables**
```sh
heroku config:set SECRET_KEY='kjasfkj123894(*##(@@@)@PO@@bfjekjewuO#2u)(UHHj@RO)r(U@!!>?>?:{KR'
heroku config:set DATABASE_URL='postgresql://neondb_owner:HgbfuWeV1JL6@ep-shy-recipe-a2bwveb5.eu-central-1.aws.neon.tech/gag_squid_print_901885'
```

### 3️⃣ **Push to Heroku**
```sh
git push heroku main
```

### 4️⃣ **Run Migrations**
```sh
heroku run python manage.py migrate
```

### 5️⃣ **Restart Heroku App**
```sh
heroku restart
```

---

## 📜 Credits

### 📷 Images
- Placeholder images sourced from **ChatGpt**, edited with GIMP.

### 📌 Code
- Bootstrap templates used for styling.
- Django documentation used for authentication and static file handling.

---

## 💙 Acknowledgements
- Special thanks to **Mo Shami** for guidance.
- Inspired by **Django tutorials and online resources**.
- Thanks to **Code Institute** for support.

##### Back to [top](#table-of-contents)

