from fastapi import FastAPI
from api.routes import router
import sys
import os
import logging

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = FastAPI()

app.include_router(router, prefix="/api")

