# LinkShare

LinkShare is a platform built with Django for sharing links. It provides a user-friendly interface for users to share and discover interesting links on various topics.

## Features

- User registration and authentication: Users can create an account, log in, and manage their profile.
- Link submission: Registered users can submit links, including a title, description, and tags.
- Link browsing: Users can browse through a collection of links, filter by tags, and search for specific keywords.
- Link details: Each link includes information such as the submitter, submission date, and user comments.
- User interaction: Users can upvote or downvote links, as well as leave comments on them.
- User profiles: Users have a profile page displaying their submitted links, comments, and voting history.
- Social sharing: Users can easily share links on social media platforms.

## Installation

Follow these steps to get LinkShare up and running on your local machine:

1. Clone the repository:

   ```
   git clone https://github.com/linkshare/linkshare.git
   ```

2. Navigate to the project directory:

   ```
   cd linkshare
   ```

3. Create a virtual environment:

   ```
   python -m venv venv
   ```

4. Activate the virtual environment:

   - For Windows:

     ```
     venv\Scripts\activate
     ```

   - For macOS/Linux:

     ```
     source venv/bin/activate
     ```

5. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

6. Set up the database:

   ```
   python manage.py migrate
   ```

7. Create a superuser account:

   ```
   python manage.py createsuperuser
   ```

8. Start the development server:

   ```
   python manage.py runserver
   ```

9. Access LinkShare in your web browser at `http://localhost:8000`.

## Contributing

Contributions are welcome! If you would like to contribute to LinkShare, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix:

   ```
   git checkout -b feature-name
   ```

3. Make your changes and commit them:

   ```
   git commit -m "Your commit message"
   ```

4. Push your changes to your forked repository:

   ```
   git push origin feature-name
   ```

5. Open a pull request in the main repository and provide a clear description of your changes.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions or suggestions, feel free to contact the project maintainer at [vincentotieno161@gmail.com](vincentotieno@gmail.com).

