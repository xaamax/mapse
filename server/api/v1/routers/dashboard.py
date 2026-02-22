from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from core.deps import get_session
from repositories import DashboardRepository
from services.dashboard_service import DashboardService

router = APIRouter()


def get_service(session: AsyncSession = Depends(get_session)) -> DashboardService:
    return DashboardService(DashboardRepository(session))


@router.get("", tags=["Dashboard"])
async def get_dashboard(service: DashboardService = Depends(get_service)):
    return await service.get_dashboard()
