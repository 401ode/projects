from django.db.utils import IntegrityError
from django.test import TestCase

from projects.models import Project


class ProjectModelTestCase(TestCase):
    """
    This is pretty weak, as tests go. We'll have to work on this.
    
    """
    

    def test_status_cannot_be_null(self):
        # Project(status=None).save()

        with self.assertRaises(IntegrityError):
            Project(status=None).save()

    def test_many_rifans_accounts_can_be_null(self):
        Project(rifans_number=None).save()
        Project(rifans_number=None).save()


class ProjectSearchTestCase(TestCase):
    def setUp(self):
        Project(rifans_number=1, name="foo bar").save()
        Project(rifans_number=2, name="foo baz", tagline="tagline!").save()

    def get_search_results(self, query):
        qs = Project.objects.search(query)
        return list(qs.values_list('rifans_number', flat=True))

    def test_basic_search(self):
        results1 = self.get_search_results('foo')
        results2 = self.get_search_results('baz')

        self.assertListEqual(results1, ['1','2'])
        self.assertListEqual(results2, ['2'])

    def test_case_insensitivity(self):
        results = self.get_search_results('FOO')
        self.assertListEqual(results, ['1', '2'])

    def test_no_results(self):
        results = self.get_search_results('gobbledygook')
        self.assertListEqual(results, [])

    def test_query_in_tagline(self):
        results = self.get_search_results('tagline')
        self.assertListEqual(results, ['2'])
