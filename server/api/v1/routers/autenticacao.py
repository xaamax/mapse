from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from schemas import UsuarioLogin

from core.configs import settings
from core.deps import get_session
from core.security import authenticate_user, create_access_token


class Token(BaseModel):
    access_token: str
    token_type: str


router = APIRouter()


@router.post("", response_model=Token)
async def login_for_access_token(
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
    return {"access_token": access_token, "token_type": "bearer"}
