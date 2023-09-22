from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def seasons(country: str, season: str):

    return {
        "country": country,
        "season": season,
    }
