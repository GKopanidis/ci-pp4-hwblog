# [HW|Blog](https://ci-pp4-hwblog-402679d73bbc.herokuapp.com/)

Welcome to HWBlog - Your Hub for Tech Enthusiasts

Dive into the HWBlog, a dedicated space for all things hardware, coding, 3D printing, Windows, and gaming. Our blog is the go-to destination for enthusiasts and professionals alike, seeking insights, tips, and discussions on the latest in technology.

**Explore Our Content:**

Hardware Haven: From the latest gadgets to in-depth hardware reviews, we’ve got you covered.
Code Corner: Discover programming tutorials, development tips, and industry best practices.
3D Printing Zone: Step into the world of 3D printing with guides, project ideas, and expert advice.
Windows Wisdom: Stay updated with Windows news, troubleshooting, and optimization techniques.
Gaming Galaxy: Join us for game reviews, previews, and everything in between for the gaming community.

![Mockup HW|Blog](docs/readme_images/Mockup_HWBlog.png)

[HW|Blog live site](https://ci-pp4-hwblog-402679d73bbc.herokuapp.com/)

### Site Goals

As a User:

- **Discover:** Explore a wide array of content on hardware, coding, 3D printing, Windows, and gaming.
- **Learn:** Benefit from tutorials, reviews, and expert insights, tailored for both novices and experienced tech enthusiasts.
- **Participate:** Join a community of like-minded individuals, share your projects, and receive feedback from peers.
- **Inspire:** Get inspired by innovative projects and creative solutions.
- **Connect:** Network with experts and hobbyists in the tech world.

As a Site Owner:

- **Educate:** Provide valuable content that keeps users at the forefront of technology and innovation.
- **Develop:** Create a platform that not only attracts tech aficionados but also fosters a community around shared interests.
- **Innovate:** Continuously enhance the site by introducing new features, content, and interactive elements to improve the user experience.
- **Support:** Offer support and resources for users to expand their skills and knowledge.
- **Expand:** Increase the site’s reach to engage a broader audience and build a more comprehensive community.

## Overview

### Existing Features

**For Users:**

- **Like Button for Blog Posts:** Implement a like button for users to express appreciation for content.

    <img src="docs/readme_images/like_button.png" width="75%" height="75%">

- **Comment on a Post:** Allow users to comment on posts to engage with content and community.

    <img src="docs/readme_images/comment_post.png" width="75%" height="75%">

- **Account Registration:** Enable users to register for an account to access personalized features.

    <img src="docs/readme_images/register.png" width="75%" height="75%">

- **View Comments:** Users can view comments on posts to read community discussions.

    <img src="docs/readme_images/view_comments.png" width="75%" height="75%">

- **Open a Post:** Provide users the ability to open and read a post in full detail.

- **Explore Paginated Post List:** Allow users to explore posts in a paginated format for better navigation.

    <img src="docs/readme_images/pagination.png" width="75%" height="75%">

- **Add Post to Favorites:** Users can add posts to a favorites list for easy access later.

    <img src="docs/readme_images/favorite_button.png" width="75%" height="75%">

- **Profile Customization:** Once logged in, users can view and customize their profile, including uploading a picture, changing their username, email, and adding an "About Me" text.

    <img src="docs/readme_images/show_profile.png" width="75%" height="75%">

    <img src="docs/readme_images/edit_profile.png" width="75%" height="75%">

- **Category Viewing and Filtering:** Users can view categories and filter posts by category or view all posts collectively.

    <img src="docs/readme_images/categories.png" width="75%" height="75%">

- **Submit Request for Collaborations:** Enable a feature for submitting collaboration requests.

    <img src="docs/readme_images/submit_request_collab.png" width="75%" height="75%">

- **Make the About Page Accessible to Users:** Ensure users can easily access and read the About page.

    <img src="docs/readme_images/about_page.png" width="75%" height="75%">

- **404 Page Visibility:** Users should encounter a user-friendly 404 page when navigating to a nonexistent link, guiding them back to the active parts of the site.

    <img src="docs/readme_images/404.png" width="75%" height="75%">

**For Site Owners:**

- **Store Collaboration Requests:** Safely store submitted collaboration requests for later review.

    <img src="docs/readme_images/admin_collab_req.png" width="75%" height="75%">

- **Mark Collaborations as Read:** Ability to mark collaborations requests as read to manage incoming queries.

    <img src="docs/readme_images/collab_mark_read.png" width="75%" height="75%">

- **Create an About Page:** Develop an About page to share the mission, vision, and team behind the site.

    <img src="docs/readme_images/create_about_page.png" width="75%" height="75%">

- **Review and Approve Comments:** Implement a system for reviewing and approving user comments to maintain a positive community environment.

    <img src="docs/readme_images/rev_and_appr_comment_1.png" width="75%" height="75%">

    <img src="docs/readme_images/rev_and_appr_comment_2.png" width="75%" height="75%">

- **Create Drafts:** Allow the creation of content drafts for future publication.

    <img src="docs/readme_images/post_draft.png" width="75%" height="75%">

- **Manage Posts:** Provide tools to manage (edit, update, delete) existing blog posts.

    <img src="docs/readme_images/manage_posts_1.png" width="75%" height="75%">


- **Modify or Delete a Post:** Enable the ability to modify or delete posts as needed.

    <img src="docs/readme_images/manage_posts_2.png" width="75%" height="75%">

- **Create Categories:** Develop a system for creating and managing post categories to organize content efficiently.

    <img src="docs/readme_images/create_cat.png" width="75%" height="75%">

### Features Planned

- Users can post content themselves, which will be displayed after approval
- Social Media Login
- Newsletter

## Design

### Wireframes

### ERD
- Entity relationship diagram was created using [DBVisualizer](https://www.dbvis.com/) and shows the schemas for each of the models and how they are related.

    <img src="docs/readme_images/ERD.jpg" width="75%" height="75%">

## Technolgies

- HTML
  - The structure of the Website was developed using HTML as the main language.
- CSS
  - The Website was styled using custom CSS in an external file.
- JavaScript
  - JavaScript was used to make the custom slider on the menu page change and the bootstrap date picker.
- Python
  - Python was the main programming language used for the application using the Django Framework.
- Visual Studio Code
  - The website was developed using Visual Studio Code IDE
- GitHub
  - Source code is hosted on GitHub
- Git
  - Used to commit and push code during the development of the Website
- Font Awesome
  - This was used for various icons throughout the site
- Favicon.io
  - favicon files were created at https://favicon.io/favicon-converter/
- balsamiq
  - wireframes were created using balsamiq from https://balsamiq.com/wireframes/desktop/#


**Python Modules Used**

- Django Class based views (ListView, UpdateView, DeleteView, CreateView) - Used for the classes to create, read, update and delete
- messages - Used to pass messages to the toasts to display feedback to the user upon actions

**External Python Modules**

- **asgiref==3.7.2:** ASGI (Asynchronous Server Gateway Interface) utilities for Python asynchronous web apps and servers.
- **cloudinary==1.36.0:** A client library for integrating Cloudinary services, enabling easy image and video management in the cloud.
- **crispy-bootstrap5==0.7:** Integrates Django forms with Bootstrap 5, providing a way to render form fields in a Bootstrap style easily.
- **dj-database-url==0.5.0:** Utility to help configure Django database settings using a URL, supporting different database engines.
- **dj3-cloudinary-storage==0.0.6:** Django 3 storage backend for Cloudinary, allowing easy file uploads to Cloudinary's cloud service.
- **Django==4.2.9:** A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- **django-allauth==0.57.0:** Authentication app for Django, providing a set of features such as social account authentication.
- **django-crispy-forms==2.1:** Django app that lets you easily build, customize, and reuse forms using your favorite CSS framework.
- **django-summernote==0.8.20.0:** Django app that integrates the Summernote WYSIWYG editor, allowing for rich text editing in forms.
- **gunicorn==20.1.0:** A Python WSGI HTTP Server for UNIX, designed to serve Python web applications from a web server.
- **oauthlib==3.2.2:** A generic, spec-compliant library to implement OAuth1 and OAuth2 providers and clients in Python.
- **psycopg2==2.9.9:** PostgreSQL database adapter for Python, providing access to PostgreSQL from Python code.
- **PyJWT==2.8.0:** A Python library to encode and decode JSON Web Tokens (JWT), used in authentication protocols.
- **python3-openid==3.2.0:** A Python 3 library for OpenID support, facilitating the implementation of OpenID authentication.
- **requests-oauthlib==1.3.1:** Provides OAuthlib authentication support for Requests, simplifying OAuth1 and OAuth2 client integration.
- **sqlparse==0.4.4:** A non-validating SQL parser for Python, useful for formatting SQL queries or extracting information from them.
- **urllib3==1.26.18:** A powerful HTTP client for Python, with features for thread safety, connection pooling, client-side SSL/TLS, and more.
- **whitenoise==5.3.0:** Simplifies static file serving for Python web apps, with integration for Django, Flask, and other WSGI apps.


## Deployment

### Version Control

The site was created using the Visual Studio Code editor and pushed to github to the remote repository ‘ci-pp4-hwblog’.

The following git commands were used throughout development to push code to the remote repo:

```git add <file>``` - This command was used to add the file(s) to the staging area before they are committed.

```git commit -m “commit message”``` - This command was used to commit changes to the local repository queue ready for the final step.

```git push``` - This command was used to push all committed code to the remote repository on github.

### Heroku Deployment

The site was deployed to Heroku. The steps to deploy are as follows:

- Navigate to heroku and create an account
- Click the new button in the top right corner
- Select create new app
- Enter app name
- Select region and click create app
- Click the resources tab and search for Heroku Postgres
- Select hobby dev and continue
- Go to the settings tab and then click reveal config vars
- Add the following config vars:
  - SECRET_KEY: (Your secret key)
  - DATABASE_URL: (This should already exist with add on of postgres)
  - CLOUNDINARY_URL: (cloudinary api url)
- Click the deploy tab
- Scroll down to Connect to GitHub and sign in / authorize when prompted
- In the search box, find the repository you want to deploy and click connect
- Scroll down to Manual deploy and choose the main branch
- Click deploy

The app should now be deployed.

The live link can be found here: [Live Site](https://ci-pp4-hwblog-402679d73bbc.herokuapp.com/)

### Run Locally

Navigate to the GitHub Repository you want to clone to use locally:

- Click on the code drop down button
- Click on HTTPS
- Copy the repository link to the clipboard
- Open your IDE of choice (git must be installed for the next steps)
- Type git clone copied-git-url into the IDE terminal

The project will now have been cloned on your local machine for use.

### Fork Project

Most commonly, forks are used to either propose changes to someone else's project or to use someone else's project as a starting point for your own idea.

- Navigate to the GitHub Repository you want to fork.

- On the top right of the page under the header, click the fork button.

- This will create a duplicate of the full project in your GitHub Repository.

## Credits

[Django Blog](https://github.com/GKopanidis/ci-pp4-wt-django-blog "Django Blog")
   - Django Blog was used as part of the education process and was referred back to for the deployment of the project

## Media

**Images**
   - AI image generator

### Acknowledgments

- Thank you to my mentor [Gareth-McGirr](https://github.com/Gareth-McGirr) who provided me with lots of pointers on resources to help on my 4th project!