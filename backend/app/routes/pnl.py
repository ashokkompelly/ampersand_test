from fastapi import APIRouter, HTTPException
from app.services.pnl_calculator import calculate_pnl
from app import state
import os

router = APIRouter()

@router.get("/pnl")
def get_pnl():
    if not state.current_file or not os.path.exists(state.current_file):
        raise HTTPException(status_code=400, detail="No file uploaded yet")

    result = calculate_pnl(state.current_file)

    response = []

    for strategy, pnl in result.items():
        response.append(
            {
                "strategy": strategy,
                "pnl": pnl
            }
        )

    return response