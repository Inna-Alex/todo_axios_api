# API
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from todos import todo

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_router = APIRouter()
api_router.include_router(todo.router, prefix="/todos", tags=["todos"])
app.include_router(api_router)
