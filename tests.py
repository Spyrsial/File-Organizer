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


class MoveFileTestCase(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp() 
        open(os.path.join(self.test_dir, "report.pdf"), "w").close()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_move_one_file(self):
        file_path = os.path.join(self.test_dir, "report.pdf")
        move_file(file_path,"Documents",self.test_dir)
        #if the movement of the file was succesful the path exists and os.path.exists returns true
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "Documents", "report.pdf")))

    def test_move_dub_file(self):
        os.makedirs(os.path.join(self.test_dir, "Documents")) # pre-existing folder for the file 
        open(os.path.join(self.test_dir, "Documents", "report.pdf"), "w").close() # pre-existing organized file 

        file_path = os.path.join(self.test_dir, "report.pdf")
        move_file(file_path,"Documents",self.test_dir)
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "Documents", "report_1.pdf")))
        
    def test_move_two_dub_files(self):
        os.makedirs(os.path.join(self.test_dir, "Documents"))  
        open(os.path.join(self.test_dir, "Documents", "report.pdf"), "w").close()  
        open(os.path.join(self.test_dir, "Documents", "report_1.pdf"), "w").close()  

        file_path = os.path.join(self.test_dir, "report.pdf")
        move_file(file_path,"Documents",self.test_dir)
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "Documents", "report_2.pdf")))
        
if __name__ == "__main__":
    unittest.main()