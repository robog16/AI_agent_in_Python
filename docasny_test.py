import unittest

from functions.get_files_info import get_files_info

class Test_Get_files_info(unittest.TestCase):
    def test_files_info_1(self):
        result = get_files_info("calculator", ".")
        expecting_result = '- main.py: file_size=719 bytes, is_dir=False\n- tests.py: file_size=1331 bytes, is_dir=False\n- pkg: file_size=44 bytes, is_dir=True'
        self.assertEqual(result, expecting_result)
    
    def test_files_info_2(self):
        result = get_files_info("calculator", "pkg")
        expecting_result = '- calculator.py: file_size=1721 bytes, is_dir=False\n- render.py: file_size=376 bytes, is_dir=False'
        self.assertEqual(result, expecting_result)
    
    def test_files_info_3(self):
        result = get_files_info("calculator", "/bin")
        expecting_result = 'Error: Cannot list "/bin" as it is outside the permitted working directory'
        self.assertEqual(result, expecting_result)
    
    def test_files_info_4(self):
        result = get_files_info("calculator", "../")
        expecting_result = 'Error: Cannot list "../" as it is outside the permitted working directory'
        self.assertEqual(result, expecting_result)

if __name__ == "__main__":
    unittest.main()