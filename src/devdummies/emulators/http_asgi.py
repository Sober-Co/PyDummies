from __future__ import annotations

def create_minimal_app():
    """[Emulator] Return a minimal Starlette app for testing webhooks.

    Requires optional dependency: Starlette.
    """
    try:
        from starlette.applications import Starlette
        from starlette.responses import JSONResponse, PlainTextResponse
        from starlette.routing import Route
    except Exception as e:
        raise RuntimeError("Install optional extra: pip install devdummies[http]") from e

    async def health(request):
        return PlainTextResponse("ok")

    async def echo(request):
        data = await request.json()
        return JSONResponse({"echo": data})

    routes = [
        Route("/health", health),
        Route("/echo", echo, methods=["POST"]),
    ]
    return Starlette(debug=False, routes=routes)
