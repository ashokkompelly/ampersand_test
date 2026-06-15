from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

import shutil
import os
from app import state


router = APIRouter()

state.current_file = None


@router.post("/upload")
async def upload_csv(
    file: UploadFile = File(...)
):

     

    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    state.current_file = file_path

    return {
        "message": "File uploaded",
        "file": file.filename
    }