from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.exception import AppException


async def app_exception_handler(request: Request, exc: AppException):
    print("HANDLER HIT")  # MUST show
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": exc.message,
            "code": getattr(exc, "code", "APP_ERROR")
        },
    )


async def generic_exception_handler(request: Request, exc: Exception):
    print("HANDLER HIT")  # MUST show
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": "Internal server error",
            "code": "INTERNAL_SERVER_ERROR",
        },
    )