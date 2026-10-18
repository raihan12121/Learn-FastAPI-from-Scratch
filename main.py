from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def RaihanApi():
    return {"Raihan" : "FastAPi"}