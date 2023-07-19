
# Store Managment

Welcome to Store Managment! This project is built with Django and requires some initial setup to get started.

## Prerequisites

Before you begin, make sure you have the following installed on your machine:

- Python (version 3.X.X)
- pip (package installer for Python)

## Installation

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/lukazibert/StoreManagement.git
   ```

2. Navigate to the project directory:

   ```shell
   cd StoreManagement
   ```

3. Create a virtual environment to isolate project dependencies:

   ```shell
   python3 -m venv env
   ```

4. Activate the virtual environment:

   - For Windows:

     ```shell
     .\env\Scripts\activate
     ```

   - For macOS/Linux:

     ```shell
     source env/bin/activate
     ```

5. Install the required dependencies:

   ```shell
   pip3 install -r requirements.txt
   ```

6. Run database migrations:

   ```shell
   python3 manage.py migrate
   ```

7. Start the development server:

   ```shell
   python3 manage.py runserver
   ```

8. Access the application in your web browser:

   ```
   http://localhost:8000/
   ```
