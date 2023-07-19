from fastapi.exceptions import HTTPException


class ApiException(HTTPException):
    pass
