from core.factories import VacancyFactory


class WantHireUseCase:

    def __init__(self, dao):
        self.dao = dao

    def execute(self, user_id, job_id, title, description, is_draft=True):
        vacancy = VacancyFactory.create(
            user_id=user_id,
            job_id=job_id,
            title=title,
            description=description,
            is_draft=is_draft,
        )
        self.dao.create(vacancy)
