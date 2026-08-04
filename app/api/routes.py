from fastapi import APIRouter, HTTPException

from app.cache.redis_cache import RedisCache
from app.core.logger import get_logger
from app.models.schemas import ResearchRequest
from app.workflows.research_graph import research_graph

router = APIRouter()

logger = get_logger(__name__)

cache = RedisCache()


@router.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "Multi-Agent Research Assistant",
    }


@router.post("/research")
def research(request: ResearchRequest):

    try:

        cache_key = request.question.strip().lower()

        cached_report = cache.get(cache_key)

        if cached_report is not None:

            logger.info(f"Cache hit: {cache_key}")

            return {
                "question": request.question,
                "report": cached_report,
                "cached": True,
            }

        logger.info(f"Cache miss: {cache_key}")

        result = research_graph.invoke(
            {
                "question": request.question,
                "plan": None,
                "findings": [],
                "report": "",
            }
        )

        cache.set(
            cache_key,
            result["report"],
            expire=3600,
        )

        logger.info("Research completed.")

        return {
            "question": request.question,
            "report": result["report"],
            "cached": False,
        }

    except Exception as e:

        logger.exception(e)

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )