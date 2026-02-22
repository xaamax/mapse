from sqlalchemy.ext.asyncio import AsyncSession


class DashboardRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    # repository is intentionally minimal; service will run queries using session
