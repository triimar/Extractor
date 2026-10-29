"""Main function to run the application"""

from fastapi import FastAPI

app = FastAPI(title="Extractor")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000)
