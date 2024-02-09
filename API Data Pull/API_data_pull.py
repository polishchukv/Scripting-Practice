from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import requests  
from apscheduler.schedulers.background import BackgroundScheduler  
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import time  
from backend.endpoints import router as api_router

# The URL of the API endpoint to fetch data from
url = "http://api.example.com/data"

def get_data():
    response = requests.get(url)  # Sending a GET request to the specified URL
    data = response.json()  # Parsing the response as JSON
    print(f"Data at {time.ctime()}: {data}")  # Printing the retrieved data along with the current time
    
app = FastAPI()  # Creating an instance of the FastAPI application
scheduler = BackgroundScheduler()  # Creating an instance of the BackgroundScheduler

scheduler.add_job(get_data, 'interval', seconds=10, max_instances=360)
# Scheduling the `get_data` function to run at a fixed interval of 10 seconds, with a maximum of 360 instances

scheduler.start()  # Starting the scheduler to begin executing the scheduled jobs

@app.get("/")
def read_root():
    return {"message": "Data retrieval is running in the background."}
# Defining a route for the root URL ("/") that returns a JSON response with a message

