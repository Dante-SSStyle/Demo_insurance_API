from app.exceptions import ApiException


class CommonClass:

    @classmethod
    def _check404(cls, query):
        if not query:
            raise ApiException(404, "Not Found")
        return query

    @classmethod
    def _check_cargo404(cls, query, cargo_type: str):
        if not query:
            raise ApiException(404, f"Cargo_type ''{cargo_type}'' Not Found")
        return query
