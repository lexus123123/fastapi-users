# from typing import TYPE_CHECKING
# from sqlalchemy import ForeignKey

# from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
# from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
# from fastapi_users_db_sqlalchemy.access_token import ( 
#     SQLAlchemyAccessTokenDatabase
# )
# from sqlalchemy.orm import Mapped, mapped_column

# from .base import Base
# from .user import User
# from core.types import UserIdType

# if TYPE_CHECKING:
#     from sqlalchemy.ext.asyncio import AsyncSession


# class AccessToken(Base, UserIdType, SQLAlchemyAccessTokenDatabase[UserIdType]):

#     __tablename__ = 'AccessTokens'

#     user_id: Mapped[UserIdType] = mapped_column(ForeignKey('users.id', ondelete='cascade'), nullable=False)

#     @classmethod  
#     def get_db(cls, session: "AsyncSession"):
#         return SQLAlchemyAccessTokenDatabase(session, AccessToken)
    










from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTable,
)
from sqlalchemy import (
    Integer,
    ForeignKey,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from core.types.user_id import UserIdType
from .base import Base

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class AccessToken(Base, SQLAlchemyBaseAccessTokenTable[UserIdType]):
    user_id: Mapped[UserIdType] = mapped_column(
        Integer,
        ForeignKey("users.id", ondelete="cascade"),
        nullable=False,
    )

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyAccessTokenDatabase(session, cls)