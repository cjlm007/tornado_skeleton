import uuid

from bootcamp.lib.json_utils import json_to_strings
from bootcamp.models.base import Model
from sqlalchemy import (
    Column,
    Integer,
    String,
)
from sqlalchemy.dialects.postgresql import JSON, UUID


class User(Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    uuid = Column(UUID, default=lambda: str(uuid.uuid4()), nullable=False)  # pragma: no cover
    user_name = Column(String(20), nullable=False)
    password = Column(String(128), nullable=False)
    email = Column(String(320), nullable=False)
    liked_titles = Column(JSON, default={}, nullable=False)  # key UUID, value Boolean
    liked_stars = Column(JSON, default={}, nullable=False)  # Key UUID, value Boolean
    play_times = Column(JSON, default={}, nullable=False)  # Key UUID, value Integer

    def to_dict(self):
        return {
            'uuid': self.uuid,
            'userName': self.user_name,
            'password': self.password,
            'email': self.email,
            'likedTitles': json_to_strings(self.liked_titles),
            'likedStars': json_to_strings(self.liked_stars),
            'playTimes': json_to_strings(self.play_times),
        }
