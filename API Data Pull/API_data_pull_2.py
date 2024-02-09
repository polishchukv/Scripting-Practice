# FastAPI = web framework
# CORSMiddleware = middleware for handling Cross-Origin Resource Sharing (CORS)
# uvicorn = ASGI server to run application
# AsyncIOScheduler = scheduler for running jobs asynchronously
# requests = library for making HTTP requests
# api_router = router for the API endpoints
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
import uvicorn
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import requests
from backend.endpoints import router as api_router

app = FastAPI()  # Creating an instance of the FastAPI application

# Adding CORS middleware allows app to handle requests from any origin, w/ any HTTP method, 
# and any HTTP headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allowing requests from any origin
    allow_credentials=True,
    allow_methods=["*"],  # Allowing all HTTP methods
    allow_headers=["*"],  # Allowing all HTTP headers
)

app.include_router(api_router, prefix='/api') # Including the router from the endpoints module

# Defining a route for the root URL ("/") that returns a JSON response with a message
@app.get("/")
def read_root():
    return {"message": "Data is being retrieved"}

# Function to call the API endpoint and retrieve data
def call_endpoint():
    response = requests.get("http://api.example.com/data")
    data = response.json()
    print(f"Data retrieved: {data}")
    
    # Here we can perform additional processing with the retrieved data, maybe upload to DB

# Creating an instance of the AsyncIOScheduler so that we can schedule jobs asynchronously    
scheduler = AsyncIOScheduler()

# Scheduling the `call_endpoint` function to run every 60 seconds
@app.on_event("startup")
async def startup_event():
    scheduler.add_job(call_endpoint, 'interval', seconds=60) # Scheduling the `call_endpoint` function to run every 60 seconds
    scheduler.start()  # Starting the scheduler to begin executing the scheduled jobs

# Running the FastAPI application using Uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
