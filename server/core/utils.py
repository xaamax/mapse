from datetime import datetime, timezone


def get_current_datetime_naive() -> datetime:
    """Retorna data/hora atual em UTC sem timezone"""
    return datetime.now(timezone.utc).replace(tzinfo=None)
