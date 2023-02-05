from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from graph.graph import graph

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/easy")
async def easy_game():
    dificulty = "facil"
    res = graph(dificulty)
    return res

@app.get("/hard")
async def hard_game():
    dificulty = "dificil"
    res = graph(dificulty)
    return res