""" Application entry point """
from app import app

# Used for development only
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
