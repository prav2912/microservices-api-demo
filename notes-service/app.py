from fastapi import FastAPI

app = FastAPI()

notes = []

@app.get("/notes")
def get_notes():
    return notes

@app.post("/notes")
def create_note(note: dict):
    notes.append(note)
    return note