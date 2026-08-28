import unittest
import os
import tempfile
import shutil
from main import categorize_file, scan_folder, move_file


class CategorizeFileTestCase(unittest.TestCase):
    def test_known_extension(self):
        self.assertEqual(categorize_file("report.pdf"), "Documents")

    def test_image_extension(self):
        self.assertEqual(categorize_file("photo.jpg"), "Images")

    def test_unknown_extension(self):
        self.assertEqual(categorize_file("data.xyz"), "Other")

    def test_no_extension(self):
        self.assertEqual(categorize_file("Makefile"), "Other")

    def test_uppercase_extension(self):
        self.assertEqual(categorize_file("photo.JPG"), "Images")
    
    def test_mixed_case_extension(self):
        self.assertEqual(categorize_file("report.pDf"), "Documents")

class ScanFolderTestCase(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory with two files and one subdirectory.
        self.test_dir = tempfile.mkdtemp()

        open(os.path.join(self.test_dir, "report.pdf"), "w").close()
        open(os.path.join(self.test_dir, "photo.jpg"), "w").close()

        os.mkdir(os.path.join(self.test_dir, "subfolder"))

    def tearDown(self):
        # Remove the temporary directory and all test contents.
        shutil.rmtree(self.test_dir)

    def test_folder_just_files(self):
        filelist = scan_folder(self.test_dir)
        self.assertEqual(len(filelist), 2)

    def test_folder_subfolder(self):
        filelist = scan_folder(self.test_dir)
        subfolder_path = os.path.join(self.test_dir, "subfolder")

        # scan_folder should return files only, not directories.
        self.assertNotIn(subfolder_path, filelist)

    def test_empty_folder(self):
        empty_dir = tempfile.mkdtemp()

        filelist = scan_folder(empty_dir)
        self.assertEqual(len(filelist), 0)

        os.rmdir(empty_dir)


class MoveFileTestCase(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        open(os.path.join(self.test_dir, "report.pdf"), "w").close()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_move_one_file(self):
        file_path = os.path.join(self.test_dir, "report.pdf")

        move_file(file_path, "Documents", self.test_dir)

        destination = os.path.join(
            self.test_dir, "Documents", "report.pdf"
        )
        self.assertTrue(os.path.exists(destination))

    def test_move_dub_file(self):
        os.makedirs(os.path.join(self.test_dir, "Documents"))

        # Simulate a filename collision in the destination folder.
        open(
            os.path.join(self.test_dir, "Documents", "report.pdf"),
            "w"
        ).close()

        file_path = os.path.join(self.test_dir, "report.pdf")

        move_file(file_path, "Documents", self.test_dir)

        renamed_file = os.path.join(
            self.test_dir, "Documents", "report_1.pdf"
        )
        self.assertTrue(os.path.exists(renamed_file))

    def test_move_two_dub_files(self):
        os.makedirs(os.path.join(self.test_dir, "Documents"))

        # Simulate two existing versions of the same filename.
        open(
            os.path.join(self.test_dir, "Documents", "report.pdf"),
            "w"
        ).close()

        open(
            os.path.join(self.test_dir, "Documents", "report_1.pdf"),
            "w"
        ).close()

        file_path = os.path.join(self.test_dir, "report.pdf")

        move_file(file_path, "Documents", self.test_dir)

        renamed_file = os.path.join(
            self.test_dir, "Documents", "report_2.pdf"
        )
        self.assertTrue(os.path.exists(renamed_file))


if __name__ == "__main__":
    unittest.main()