from fastapi import FastAPI
from app.routers import message_router

app = FastAPI()

# Include the message router
app.include_router(message_router.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
