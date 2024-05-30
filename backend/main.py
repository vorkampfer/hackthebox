"import asyncio

from fastapi import FastAPI, APIRouter, Query, HTTPException, Request, Depends
from fastapi_contrib.common.responses import UJSONResponse
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi



from typing import Optional, Any
from pathlib import Path
from sqlalchemy.orm import Session



from app.schemas.user import User
from app.api.v1.api import api_router
from app.core.config import settings

from app import deps
from app import crud


app = FastAPI(title="UHC API Quals", openapi_url=None, docs_url=None, redoc_url=None)
root_router = APIRouter(default_response_class=UJSONResponse)


@app.get("", status_code=200)
def root():
    """
    Root GET
    """
    return {"msg": "UHC API Version 1.0"}


@app.get("/api", status_code=200)
def list_versions():
    """
    Versions
    """
    return {"endpoints":["v1"]}


@app.get("/api/v1", status_code=200)
def list_endpoints_v1():
    """
    Version 1 Endpoints
    """
    return {"endpoints":["user", "admin"]}


@app.get("/docs")
async def get_documentation(
    current_user: User = Depends(deps.parse_token)
    ):
    return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")

@app.get("/openapi.json")
async def openapi(
    current_user: User = Depends(deps.parse_token)
):
    return get_openapi(title = "FastAPI", version="0.1.0", routes=app.routes)

app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(root_router)

def start():
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
"
