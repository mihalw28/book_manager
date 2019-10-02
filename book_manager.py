from app import create_app, db
from app.models import Book

app = create_app()

if __name__ == "__main__":
    app.run()


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Book": Book}
