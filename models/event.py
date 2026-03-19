from sqlalchemy.orm import Mapped, mapped_column
from db import Base


class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    action: Mapped[str] = mapped_column()
    target_type: Mapped[str] = mapped_column()
    data: Mapped[str] = mapped_column()

    def to_dict(self):
        return {
            "id": self.id,
            "action": self.action,
            "target_type": self.target_type,
            "data": self.data,
        }

    def get_id(self):
        return str(self.id)