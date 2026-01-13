from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlmodel import Session, select

from database import create_db_and_tables, get_session
from models import Post

app = FastAPI(title="Bytelaugh API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (JS, CSS, images)
app.mount(
    "/static", 
    StaticFiles(directory="../frontend/pages", html=True),
    name="static"
)

# Serve HTML pages
@app.get("/")
async def read_root():
    from fastapi.responses import HTMLResponse
    with open("../frontend/pages/index.html", encoding="utf-8") as f:
        content = f.read()
    return HTMLResponse(content=content, media_type="text/html; charset=utf-8")

@app.get("/feed.html")
async def read_feed():
    from fastapi.responses import HTMLResponse
    with open("../frontend/pages/feed.html", encoding="utf-8") as f:
        content = f.read()
    return HTMLResponse(content=content, media_type="text/html; charset=utf-8")

@app.get("/create.html")
async def read_create():
    from fastapi.responses import HTMLResponse
    with open("../frontend/pages/create.html", encoding="utf-8") as f:
        content = f.read()
    return HTMLResponse(content=content, media_type="text/html; charset=utf-8")

# Specific handlers for static files that need to be accessed from root path
@app.get("/js/{file_name}")
async def read_js(file_name: str):
    import os
    file_location = f"../frontend/pages/js/{file_name}"
    if os.path.exists(file_location) and os.path.isfile(file_location):
        from fastapi.responses import FileResponse
        return FileResponse(file_location)
    from fastapi.responses import PlainTextResponse
    return PlainTextResponse("Not Found", status_code=404)

@app.get("/css/{path:path}")
async def read_css(path: str):
    import os
    file_location = f"../frontend/pages/css/{path}"
    if os.path.exists(file_location) and os.path.isfile(file_location):
        from fastapi.responses import FileResponse
        return FileResponse(file_location)
    from fastapi.responses import PlainTextResponse
    return PlainTextResponse("Not Found", status_code=404)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/api/posts")
def get_posts(session: Session = Depends(get_session)):
    return session.exec(
        select(Post).order_by(Post.created_at.desc())
    ).all()

@app.post("/api/posts", status_code=201)
def create_post(post: dict, session: Session = Depends(get_session)):
    content = post.get("content", "").strip()

    if not content:
        raise HTTPException(status_code=400, detail="Post content required")

    new_post = Post(content=content)
    session.add(new_post)
    session.commit()
    session.refresh(new_post)

    return new_post
