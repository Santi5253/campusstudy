import httpx, asyncio
from core.config import settings

async def get_json(base_url: str, path: str, token: str | None = None):
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    last_error = None
    for intento in range(3):
        try:
            async with httpx.AsyncClient(timeout=settings.request_timeout) as client:
                r = await client.get(f"{base_url}{path}", headers=headers)
                r.raise_for_status()
                return r.json()
        except (httpx.TimeoutException, httpx.ConnectError) as e:
            last_error = e
            await asyncio.sleep(0.5 * (2 ** intento))
    raise last_error
