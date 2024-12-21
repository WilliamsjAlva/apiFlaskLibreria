from app import db, createApp

app = createApp()

if __name__ == "__main__":
    app.run(debug=True, port=7000)

with app.app_context():
    db.create_all()
