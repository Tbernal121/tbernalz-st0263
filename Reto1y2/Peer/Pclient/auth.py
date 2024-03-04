import requests
from dotenv import load_dotenv
import os
load_dotenv()

central_server = os.getenv("CENTRAL_SERVER_URL")

def login():
    try:
        requests.get(central_server+"login")
    except:
        print("Central server is not available. Please try again later.")
        exit(0)

    print("Logging in...")

def logout():
    print("Logging out...")
    exit(0)