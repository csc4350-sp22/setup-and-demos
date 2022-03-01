import unittest
from unittest.mock import MagicMock, patch
from wiki import get_wiki_link


class WikiTests(unittest.TestCase):
    def test_get_wiki_link(self):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "query": {"pages": {"id1": {"fullurl": "google.com"}}}
        }
        with patch("wiki.requests.get") as mock_get:
            mock_get.return_value = mock_response
            result = get_wiki_link("movie_name")
            self.assertEqual(result, "google.com")


if __name__ == "__main__":
    unittest.main()
