import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class RepositoryTests(unittest.TestCase):

    def test_readme_exists(self):
        self.assertTrue((ROOT / "README.md").is_file())

    def test_author_details_are_present(self):
        readme = (ROOT / "README.md").read_text()
        self.assertIn("24ESKCS091", readme)
        self.assertIn("BHUPENDRA SOU", readme)
        self.assertIn("bhupendrasou", readme)

    def test_project_name_is_present(self):
        readme = (ROOT / "README.md").read_text()
        self.assertIn("Personal Expense Manager", readme)

    def test_gitignore_excludes_dependencies(self):
        gitignore = (ROOT / ".gitignore").read_text()
        self.assertIn("node_modules/", gitignore)
        self.assertIn(".env", gitignore)
        self.assertIn(".DS_Store", gitignore)


if __name__ == "__main__":
    unittest.main()
