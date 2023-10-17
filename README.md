# Django Chat App

A simple real-time chat application built with Django and Channels.

## Overview

This chat app allows users to participate in real-time chat rooms. Users can send and receive messages in the chat rooms, creating a dynamic and interactive chatting experience.

## Features

- User registration and authentication.
- Real-time messaging using Django Channels.
- Multiple chat rooms.
- Admin interface for managing chat rooms and users.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/hrudaydeep24/chatapp.git
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install project dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the chat app at [http://127.0.0.1:8000/chat/](http://127.0.0.1:8000/chat/).

## Usage

1. Register an account or log in to an existing account.
2. Browse and join existing chat rooms.
3. Start chatting in real time with other users in the selected chat room.

## Admin Interface

- Access the admin panel at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).
- Log in with the superuser credentials.


## Contributing

Feel free to contribute to this project. You can open issues, submit pull requests, or suggest improvements and new features.

```
