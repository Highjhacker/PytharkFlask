from app import create_app
import os

app = create_app(os.getenv('APP_SETTINGS'))

app.run()
