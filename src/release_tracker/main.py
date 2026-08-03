from fastapi import FastAPI

app = FastAPI(ftitle="Release Tracker API")


@app.get("/projects")
def list_projects() -> list[dict]:
    return [{"id": 1, "name": "Example"}]
