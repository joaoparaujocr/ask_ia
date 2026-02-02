import uvicorn

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Root"

def main():
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_level="info",
        reload=True
    )

if __name__ == "__main__":
    main()
