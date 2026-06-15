from fastapi import FastAPI
from app.routes.upload import router as upload_router
from app.routes.pnl import router as pnl_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Trade PnL Service"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router)
app.include_router(pnl_router)