import json
from datetime import datetime, timezone, timedelta

from sqlalchemy import Column, Integer, String, Enum as SQLAlchemyEnum, DateTime

from board_policy import BoardPolicy
from enum.board_status import BoardStatus
from persistence.session import Base

KST = timezone(timedelta(hours=9))


class Board(Base):
    __tablename__ = "board"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    policy = Column(String(255), index=True)
    started_at = Column(DateTime, index=True)
    ended_at = Column(DateTime, index=True)
    status = Column(SQLAlchemyEnum(BoardStatus), default=BoardStatus.DISABLED)
    created_by = Column(String(50))
    updated_by = Column(String(50))
    created_at = Column(DateTime, default=datetime.now(KST))
    updated_at = Column(DateTime, default=datetime.now(KST))

    def set_policy(self, policy):
        self.policy = json.dumps(policy.__dict__)

    def get_policy(self) -> BoardPolicy:
        try:
            policy_dict = json.loads(self.policy)
            return BoardPolicy(**policy_dict)
        except (json.JSONDecodeError, TypeError) as e:
            raise ValueError("") from e
