from fastapi import FastAPI


app = FastAPI(
    title="Airbnb Sentiment API"
)

@app.get("/")
async def hello_world():
    return {"message": "Hola Mundo"}


