# BLog Website

This is a Django project that allows users to create, edit, and publish blog posts using the Summernote editor.

## Setup

1. Clone the repository:

    ```bash
    https://github.com/MuhammadNasarUddin/blogwebsite/
    ```

2. Navigate to the project directory:

    ```bash
    cd blog
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser account to access the admin panel:

    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:

    ```bash
    python manage.py runserver
    ```

7. Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the application.

## Features

- **Home**: Display a list of blog posts with a search functionality.
- **Blog**: Allow users to create new blog posts using the Summernote editor.
- **Detail**: View the details of a specific blog post.
- **User Blog Detail**: View and manage blog posts created by the logged-in user.
- **User Blog Edit**: Edit existing blog posts.
- **User Blog Delete**: Delete existing blog posts.
- **Sign In/Sign Up/Sign Out**: Authentication functionality.

## Usage

1. Create a superuser account using the `createsuperuser` command.

2. Log in to the admin panel at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) using the superuser credentials.

3. Create blog posts using the Summernote editor in the admin panel.

4. View, edit, and delete your own blog posts through the user interface.
