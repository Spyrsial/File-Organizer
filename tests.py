import unittest
import os
import tempfile
import shutil
from main import categorize_file, scan_folder

class CategorizeFileTestCase(unittest.TestCase):
    def test_known_extension(self):
        self.assertEqual(categorize_file("report.pdf"), "Documents")
    
    def test_image_extension(self):
        self.assertEqual(categorize_file("photo.jpg"), "Images")
    
    def test_unknown_extension(self):
        self.assertEqual(categorize_file("data.xyz"), "Other")
    
    def test_no_extension(self):
        self.assertEqual(categorize_file("Makefile"), "Other")


class ScanFolderTestCase(unittest.TestCase):
    def setUp(self):
        # create a temp folder
        self.test_dir = tempfile.mkdtemp() 
        # create fake files
        open(os.path.join(self.test_dir, "report.pdf"), "w").close()
        open(os.path.join(self.test_dir, "photo.jpg"), "w").close()
        # create fake subfolder
        os.mkdir(os.path.join(self.test_dir, "subfolder"))

    # deleting everything we created
    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_folder_just_files(self):
        filelist = scan_folder(self.test_dir)
        self.assertEqual(len(filelist), 2)

    # is the subfolder inside the list that scan_folder creates ?
    # (we already know from the test before but Explicit is better than implicit)
    def test_folder_subfolder(self):
        filelist = scan_folder(self.test_dir)
        subfolder_path = os.path.join(self.test_dir, "subfolder")
        self.assertNotIn(subfolder_path, filelist)

    def test_empty_folder(self):
        empty_dir = tempfile.mkdtemp() # creating a new empty folder
        filelist = scan_folder(empty_dir)
        self.assertEqual(len(filelist), 0) 
        os.rmdir(empty_dir) # deleting the new folder

    
if __name__ == "__main__":
    unittest.main()