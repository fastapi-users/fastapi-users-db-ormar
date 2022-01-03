import uuid
import asyncio
from typing import Optional, List

import pytest
from fastapi_users import models
from pydantic import BaseModel, UUID4, Field


class Role(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4)
    name: str


class User(models.BaseUser):
    first_name: Optional[str]
    roles: Optional[List[Role]]


class UserCreate(models.BaseUserCreate):
    first_name: Optional[str]
    roles: Optional[List[Role]]


class UserUpdate(models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    pass


class UserOAuth(User, models.BaseOAuthAccountMixin):
    pass


class UserDBOAuth(UserOAuth, UserDB):
    pass


@pytest.fixture(scope="session")
def event_loop():
    """Force the pytest-asyncio loop to be the main one."""
    loop = asyncio.get_event_loop()
    yield loop


@pytest.fixture
def oauth_account1() -> models.BaseOAuthAccount:
    return models.BaseOAuthAccount(
        oauth_name="service1",
        access_token="TOKEN",
        expires_at=1579000751,
        account_id="user_oauth1",
        account_email="king.arthur@camelot.bt",
    )


@pytest.fixture
def oauth_account2() -> models.BaseOAuthAccount:
    return models.BaseOAuthAccount(
        oauth_name="service2",
        access_token="TOKEN",
        expires_at=1579000751,
        account_id="user_oauth2",
        account_email="king.arthur@camelot.bt",
    )
