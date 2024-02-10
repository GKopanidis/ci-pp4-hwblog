## Manual Testing

| Feature                                         | Expectation                                                                                          | Action                                                                                     | Result                                                                           |
|-------------------------------------------------|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| **Non-Logged-In User**                          |                                                                                                      |                                                                                            |                                                                                  |
| Home Page Display                               | Users should be able to view the home page                                                           | Navigate to the home page                                                                  | Home page is visible                                                            |
| About Page Accessibility                        | Users should be able to access and read the About page                                               | Navigate to the About page                                                                 | About page is visible and readable                                              |
| Profile Page Access                             | Users should be redirected to login when trying to access profile page                               | Click on the profile page link                                                             | Redirected to login page                                                        |
| Register Page Display                           | Users should be able to access the registration page                                                 | Navigate to the registration page                                                          | Registration page is visible                                                    |
| Login Page Display                              | Users should be able to access the login page                                                        | Navigate to the login page                                                                 | Login page is visible                                                           |
| Open a Post                                     | Users should be able to open and read a post in full detail                                          | Click on a post                                                                            | Post opens and all details are visible                                          |
| Category Links                                  | Users should be able to click on category links and see corresponding posts                          | Click on a category link                                                                   | Posts filtered by the selected category are displayed                          |
| 404 Page Visibility                             | All users should encounter a user-friendly 404 page when navigating to a nonexistent link           | Navigate to a nonexistent link                                                             | User-friendly 404 page is displayed                                             |
| **Logged-In User**                              |                                                                                                      |                                                                                            |                                                                                  |
| Comment Submission                              | Logged-in users should be able to submit comments on posts                                           | Submit a comment on a post                                                                 | Comment is submitted and displays "Awaiting approval"                           |
| Edit/Delete Comment                             | Users should see Edit and Delete buttons for their own comments                                      | View a post you have commented on                                                          | Edit and Delete buttons are visible for user's own comments                     |
| Like/Unlike Post                                | Users should be able to like or unlike a post                                                        | Click on the "Like" or "Unlike" button on a post                                           | Post is liked or unliked, respectively                                          |
| Favorite/Unfavorite Post                        | Users should be able to add or remove a post from their favorites list                               | Click on the "Favorite" or "Unfavorite" button on a post                                   | Post is added to or removed from the user's favorites list                      |
| Profile Page Display                            | Users should be able to view their profile page                                                      | Navigate to the profile page                                                               | Profile page is visible                                                         |
| Profile Customization                           | Users should be able to customize their profile image and "About me" text                            | Navigate to the profile edit page and make changes                                         | Changes are saved and reflected in the profile                                  |
| Favorites Link                                  | "Favorites" link should be visible and clickable                                                     | Click on the "Favorites" link                                                              | Favorites page is visible with all favorited posts                              |
| Logout Functionality                            | "Logout" button should log the user out and display a confirmation message                          | Click on the "Logout" button                                                               | User is logged out with a confirmation message displayed                        |
| **Staff User**                                  |                                                                                                      |                                                                                            |                                                                                  |
| All functions available to Logged-In Users      | Staff users should have access to all functionalities available to logged-in users                  | Perform actions available to logged-in users                                               | All functionalities work as expected                                            |
| Create Post Button                              | "Create Post" button should be visible to staff users on the home page                              | Click on the "Create Post" button                                                          | Post creation form is displayed                                                 |
| Post Creation                                   | Staff users should be able to create a new post                                                      | Fill out the post creation form and save                                                   | New post is created and displayed in the post list                              |
| Approve Comments                                | Staff or superusers should be able to approve comments                                               | Click the "Approve" button next to an unapproved comment                                    | Comment is approved and visible to all users                                    |
| Edit/Delete Buttons on Post                     | Edit and Delete buttons should be visible for staff users on their posts                             | View a post created by the staff user                                                      | Edit and Delete buttons are visible                                             |
| Admin Area Access                               | Staff users should have access to the Django admin panel for allowed functionalities                | Navigate to the Django admin panel                                                         | Allowed functionalities are accessible and functional                           |
| **Superuser**                                   |                                                                                                      |                                                                                            |                                                                                  |
| All functions available to Staff Users          | Superusers should have access to all functionalities available to staff users                       | Perform actions available to staff users                                                   | All functionalities work as expected                                            |
| Full Admin Area Access                          | Superusers should have full access to all functionalities in the Django admin panel                 | Navigate to the Django admin panel                                                         | All functionalities are accessible and functional                               |


## Additional Validation Testing

In addition to the accessibility tests, several other tests were conducted to ensure the code quality and standard compliance of the project.

### W3C Testing

- **HTML**: Passed without any remarks.

  <img src="docs/readme_images/w3c.png" width="75%" height="75%">

- **CSS**: Passed without any remarks.

  <img src="docs/readme_images/w3c_css.png" width="75%" height="75%">

### JSHint Testing

- **JavaScript** code was analyzed using JSHint and passed without any remarks.

  <img src="docs/readme_images/jshint.png" width="75%" height="75%">


### PEP8 Testing

Python code was analyzed using PEP8 and passed without any remarks with the [CodeInstitute Python Linter](https://pep8ci.herokuapp.com/)

## Lightouse score

- **Index.html**

  <img src="docs/readme_images/html_index.png" width="75%" height="75%">

- **About.html**

  <img src="docs/readme_images/html_about.png" width="75%" height="75%">

- **Profile.html**

  <img src="docs/readme_images/html_profile.png" width="75%" height="75%">

- **Register.html**

  <img src="docs/readme_images/html_register.png" width="75%" height="75%">

- **Login.html**

  <img src="docs/readme_images/html_login.png" width="75%" height="75%">


## Tested Browser
   - Latest versions:
     <table>
       <thead>
       <tr>
       <th align="center">Browser</th>
       <th align="center">Layout</th>
       <th align="center">Functionality</th>
       </tr>
       </thead>
       <tbody>
         <tr>
         <td align="center">Chrome</td>
         <td align="center">✔</td>
         <td align="center">✔</td>
         </tr>
         <tr>
         <td align="center">Edge</td>
         <td align="center">✔</td>
         <td align="center">✔</td>
         </tr>
         <tr>
         <td align="center">Firefox</td>
         <td align="center">✔</td>
         <td align="center">✔</td>
         </tr>
         <tr>
         <td align="center">Safari</td>
         <td align="center">✔</td>
         <td align="center">✔</td>
         </tr>
       </tbody>
     </table>