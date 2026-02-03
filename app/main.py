import uvicorn

from fastapi import FastAPI
from routes.api.question_and_answer import router as question_and_answer

app = FastAPI()

app.include_router(question_and_answer)

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
