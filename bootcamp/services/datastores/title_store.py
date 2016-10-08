from bootcamp.lib.database import get_db_session
from bootcamp.models.title import Title


class TitleStore(object):
    def get_titles(self):
        query = Title.query()
        models = [_ for _ in query]
        return models

    def get_title(self, uuid):
        query = Title.query().filter(Title.uuid == uuid)
        return query

    def create_from_entity(self, title):
        new_title = Title(
            uuid=title.uuid,
            created_at=title.created_at,
            updated_at=title.updated_at,
            title_id=title.title_id,
            title=title.title,
            video_path=title.video_path,
            file_names=title.file_names,
            description=title.description,
            video_size=title.video_size,
            rate=title.rate,
        )
        new_title.validate()
        self.commit()
        return Title.to_entity(new_title)

    @staticmethod
    def commit():
        get_db_session().commit()
