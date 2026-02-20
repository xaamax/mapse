from datetime import datetime, timedelta, timezone
from typing import Optional

from fastapi import Depends, HTTPException, status, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from passlib.hash import bcrypt
from sqlalchemy.ext.asyncio import AsyncSession

from core.configs import settings
from core.deps import get_session
from models import Usuario
from repositories import UsuarioRepository
from core.exceptions import UnauthorizedException


class CustomHTTPBearer(HTTPBearer):
    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials:
        try:
            return await super().__call__(request)
        except HTTPException as e:
            if e.status_code == status.HTTP_401_UNAUTHORIZED:
                raise UnauthorizedException("As credenciais de autenticação não foram fornecidas")
            raise


http_bearer = CustomHTTPBearer()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return bcrypt.using(rounds=settings.BCRYPT_ROUNDS).hash(password)


async def authenticate_user(
    email: str,
    password: str,
    session: AsyncSession,
) -> Optional[Usuario]:
    repository = UsuarioRepository(session)
    user = await repository.get_by_email(email)
    if not user:
        return None
    if not verify_password(password, user.senha):
        return None
    # Re-hash password if hashing parameters were updated
    try:
        if bcrypt.using(rounds=settings.BCRYPT_ROUNDS).needs_update(user.senha):
            user.senha = get_password_hash(password)
            await repository.update(user)
    except Exception:
        # avoid failing authentication due to re-hash issues
        pass
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode,
        settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM,
    )
    return encoded_jwt


async def get_current_user(
    token: HTTPAuthorizationCredentials = Depends(http_bearer),
    session: AsyncSession = Depends(get_session),
) -> Usuario:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possível validar as credenciais",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token.credentials,
            settings.JWT_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM],
        )
        email: str | None = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    repository = UsuarioRepository(session)
    user = await repository.get_by_email(email)
    if not user or not user.ativo:
        raise credentials_exception

    return user
