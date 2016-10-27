from unittest import TestCase
from unittest.mock import Mock, patch

from core.use_cases import WantHireUseCase


class WantHireUseCaseTestCase(TestCase):

    def setUp(self):
        patcher = patch('core.use_cases.want_hire_use_case.VacancyFactory')
        self.factory = patcher.start()
        self.addCleanup(patcher.stop)

        self.vacancy = Mock() # TODO: Mock behavior
        self.factory.create.return_value = self.vacancy

        self.dao = Mock()
        self.use_case = WantHireUseCase(self.dao)

        self.data = {
            'job_id': 1,
            'user_id': 2,
            'title': 'Title',
            'description': 'Description',
        }

    def test_execute_creates_vacancy_correctly(self):
        self.use_case.execute(**self.data)
        self.factory.create.assert_called_once_with(is_draft=True, **self.data)
        self.dao.create.assert_called_once_with(self.vacancy)

    def test_execute_creates_vacancy_with_draft_param_correctly(self):
        self.use_case.execute(is_draft=False, **self.data)
        self.factory.create.assert_called_once_with(is_draft=False, **self.data)
        self.dao.create.assert_called_once_with(self.vacancy)
