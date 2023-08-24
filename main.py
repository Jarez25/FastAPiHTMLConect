from fastapi import FastAPI as FP
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles

app = FP()

app.mount("/public", StaticFiles(directory="public"), name="static")


@app.get('/index', response_class=HTMLResponse)
def root():
    html_address = "public/index.html"
    return FileResponse(html_address)
