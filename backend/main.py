from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Any, Dict

from database import create_document
from schemas import Lead, DemoRequest

app = FastAPI(title="LandlordLink API", version="1.0.0")

# CORS to allow frontend calls
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class SuccessResponse(BaseModel):
    ok: bool
    message: str
    data: Dict[str, Any] | None = None


@app.get("/health", response_model=SuccessResponse)
async def health():
    return SuccessResponse(ok=True, message="OK", data=None)


@app.post("/api/leads", response_model=SuccessResponse)
async def create_lead(lead: Lead):
    try:
        inserted_id = create_document("lead", lead)
        return SuccessResponse(ok=True, message="Lead captured", data={"id": inserted_id})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/demo-requests", response_model=SuccessResponse)
async def create_demo_request(payload: DemoRequest):
    try:
        inserted_id = create_document("demorequest", payload)
        return SuccessResponse(ok=True, message="Demo request received", data={"id": inserted_id})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
