from pathlib import Path
from openapi_to_fastapi.routes import SpecRouter

specs = Path("./specs")

router = SpecRouter(specs).to_fastapi_router()