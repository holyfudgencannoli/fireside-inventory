from flask.config import T
from sqlalchemy import Column, Integer, String, null
from sqlalchemy.orm import Mapped, mapped_column

from db import Base


class Authenticator(Base):
    __tablename__ = "authenticators"

    id: Mapped[str] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(nullable=False)
    provider: Mapped[str] = mapped_column(nullable=False)
    provider_account_id: Mapped[str] = mapped_column(nullable=True)
    access_token_hash: Mapped[str] = mapped_column(nullable=True)
    refresh_token_hash: Mapped[str] = mapped_column(nullable=True)
    expires_at: Mapped[int] = mapped_column(nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "provider": self.provider,
            "provider_account_id": self.provider_account_id,
            "access_token_hash": self.access_token_hash,
            "refresh_token_hash": self.refresh_token_hash,
            "expires_at": self.expires_at
        }

    def get_id(self):
        return str(self.id)