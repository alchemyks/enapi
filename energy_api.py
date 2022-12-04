from energy_scraping import get_addresses
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return get_addresses()
