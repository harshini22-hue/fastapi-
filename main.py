import fastapi
from fastapi import FastAPI
app = FastAPI()
import uvicorn

@app.get("/Employee")
async def root(name:str):
    return {"name": name, "EmpId": 2212, "Age":21}

if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
