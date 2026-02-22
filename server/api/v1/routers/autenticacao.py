from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from models import UsuarioLogin

from core.configs import settings
from core.deps import get_session
from core.security import authenticate_user, create_access_token


router = APIRouter()


@router.post("")
async def login(
    payload: UsuarioLogin,
    session: AsyncSession = Depends(get_session),
):
    user = await authenticate_user(payload.email, payload.senha, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário ou senha inválidos"
        )

    access_token_expires = timedelta(
        minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    )
    access_token = create_access_token(
        data={"sub": user.email},
        expires_delta=access_token_expires,
    )

    refresh_token_expires = timedelta(
        minutes=settings.JWT_REFRESH_TOKEN_EXPIRE_MINUTES
    )
    refresh_token = create_access_token(
        data={"sub": user.email, "type": "refresh"},
        expires_delta=refresh_token_expires,
    )

    expires_in = datetime.now(timezone.utc) + access_token_expires
    expires_in_str = expires_in.strftime("%Y-%m-%dT%H:%M:%SZ")

    return {
        "access": access_token,
        "refresh": refresh_token,
        "expiresIn": expires_in_str,
    }
