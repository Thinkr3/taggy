import unittest
from exif_editor import ExifEditor

class TestKeywordReader(unittest.TestCase):

    global jpg
    global png
    jpg = ExifEditor("ramen.jpg")
    png = ExifEditor("scientist.png")

    def setUp(self):
        jpg.clear_keywords()
        png.clear_keywords()

    def test_add_keyword(self):
        jpg.add_keyword("soup")
        png.add_keyword("bow")
        self.assertEqual(jpg.keywords, ["soup"])
        self.assertEqual(png.keywords, ["bow"])

    def test_add_multiple_keywords(self):
        jpg.add_keyword("soup")
        jpg.add_keyword("ramen")
        png.add_keyword("bow")
        png.add_keyword("arrow")
        self.assertEqual(jpg.keywords, ["soup", "ramen"])
        self.assertEqual(png.keywords, ["bow", "arrow"])

    def test_add_duplicate_keywords(self):
        jpg.add_keyword("soup")
        jpg.add_keyword("soup")
        png.add_keyword("bow")
        png.add_keyword("bow")
        self.assertEqual(jpg.keywords, ["soup"])
        self.assertEqual(png.keywords, ["bow"])

    def test_add_keywords_with_semicolons(self):
        jpg.add_keyword("soup;ramen")
        png.add_keyword("bow;arrow")
        self.assertEqual(jpg.keywords, ["soup", "ramen"])
        self.assertEqual(png.keywords, ["bow", "arrow"])

    def test_add_keywords_with_semicolons_and_spaces(self):
        jpg.add_keyword("soup; ramen")
        png.add_keyword("bow; arrow")
        self.assertEqual(jpg.keywords, ["soup", "ramen"])
        self.assertEqual(png.keywords, ["bow", "arrow"])

    def test_add_keywords_with_semicolons_and_spaces_and_duplicates(self):
        jpg.add_keyword("soup; ramen")
        jpg.add_keyword("soup; ramen")
        png.add_keyword("bow; arrow")
        png.add_keyword("bow; arrow")
        self.assertEqual(jpg.keywords, ["soup", "ramen"])
        self.assertEqual(png.keywords, ["bow", "arrow"])

    def test_add_keywords_with_semicolons_and_spaces_and_duplicates_and_multiple_keywords(self):
        jpg.add_keyword("soup; ramen")
        jpg.add_keyword("soup; ramen")
        jpg.add_keyword("soup")
        jpg.add_keyword("ramen")
        png.add_keyword("bow; arrow")
        png.add_keyword("bow; arrow")
        png.add_keyword("bow")
        png.add_keyword("arrow")
        self.assertEqual(jpg.keywords, ["soup", "ramen"])
        self.assertEqual(png.keywords, ["bow", "arrow"])

    def test_add_keywords_with_semicolons_and_spaces_and_duplicates_and_multiple_keywords_and_remove_duplicates(self):
        jpg.add_keyword("soup; ramen")
        jpg.add_keyword("soup; ramen")
        jpg.add_keyword("soup")
        jpg.add_keyword("ramen")
        jpg.remove_keyword("soup")
        jpg.remove_keyword("ramen")
        png.add_keyword("bow; arrow")
        png.add_keyword("bow; arrow")
        png.add_keyword("bow")
        png.add_keyword("arrow")
        png.remove_keyword("bow")
        png.remove_keyword("arrow")
        self.assertEqual(jpg.keywords, [])
        self.assertEqual(png.keywords, [])

    def test_remove_keyword(self):
        jpg.add_keyword("soup")
        jpg.remove_keyword("soup")
        png.add_keyword("bow")
        png.remove_keyword("bow")
        self.assertEqual(jpg.keywords, [])
        self.assertEqual(png.keywords, [])

    def test_remove_multiple_keywords(self):
        jpg.add_keyword("soup")
        jpg.add_keyword("ramen")
        jpg.remove_keyword("soup")
        jpg.remove_keyword("ramen")
        png.add_keyword("bow")
        png.add_keyword("arrow")
        png.remove_keyword("bow")
        png.remove_keyword("arrow")
        self.assertEqual(jpg.keywords, [])
        self.assertEqual(png.keywords, [])

    def test_remove_keyword_not_in_list(self):
        jpg.add_keyword("soup")
        jpg.remove_keyword("ramen")
        png.add_keyword("bow")
        png.remove_keyword("arrow")
        self.assertEqual(jpg.keywords, ["soup"])
        self.assertEqual(png.keywords, ["bow"])

    def test_remove_keyword_with_semicolons(self):
        jpg.add_keyword("soup; ramen")
        jpg.remove_keyword("soup")
        png.add_keyword("bow; arrow")
        png.remove_keyword("bow")
        self.assertEqual(jpg.keywords, ["ramen"])
        self.assertEqual(png.keywords, ["arrow"])

    def tearDown(self):
        jpg.close_image()
        png.close_image()


if __name__ == '__main__':
    unittest.main()
    
