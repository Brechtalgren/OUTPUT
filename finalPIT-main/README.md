# Bytelaugh - Microblogging Application

A simple microblogging platform built with FastAPI, SQLModel, and Axios.

## Features

- Create and share short text posts
- View all posts in chronological order
- Modern UI with responsive design
- SQLite database for data persistence

## Requirements

- Python 3.7+
- pip (Python package installer)

## Installation

1. **Clone or download the project**

2. **Navigate to the backend directory**
   ```bash
   cd bytelaugh(updated)/backend
   ```

3. **Install the required Python packages**
   ```bash
   pip install fastapi uvicorn sqlmodel
   ```

4. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```

## Usage

1. **Open a terminal/command prompt**

2. **Navigate to the backend directory**
   ```bash
   cd bytelaugh(updated)/backend
   ```

3. **Install the required Python packages** (if not already installed)
   ```bash
   pip install fastapi uvicorn sqlmodel
   ```

4. **Start the server**
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the application**
   Open your browser and go to `http://127.0.0.1:8000`
   
   Note: If port 8000 is busy, you can specify a different port:
   ```bash
   uvicorn main:app --port 8001 --reload
   ```
   or
   ```
   uvicorn main:app --port 8000
   
   ```
   Then access via `http://127.0.0.1:8001`

6. **Using the application**
   - Visit the home page to get started
   - Click "Create" to write a new post
   - Click "Feed" to view all posts

## Project Structure

```
bytelaugh(updated)/
├── backend/
│   ├── main.py          # FastAPI application
│   ├── database.py      # Database configuration
│   ├── models.py        # SQLModel definitions
│   └── posts.db         # SQLite database (generated automatically)
└── frontend/
    └── pages/           # HTML, CSS, and JavaScript files
        ├── index.html
        ├── feed.html
        ├── create.html
        ├── css/
        └── js/
```

## API Endpoints

- `GET /api/posts` - Retrieve all posts
- `POST /api/posts` - Create a new post

## Technologies Used

- **Backend**: FastAPI, SQLModel, SQLite
- **Frontend**: HTML, CSS, JavaScript, Axios
- **Database**: SQLite (file-based)

## Troubleshooting

If you encounter any issues:

1. Make sure all dependencies are installed: `pip install fastapi uvicorn sqlmodel`
2. Ensure the backend server is running when accessing the frontend
3. Check that the `posts.db` file has proper read/write permissions
4. If emojis or special characters don't display correctly, ensure your files are saved with UTF-8 encoding