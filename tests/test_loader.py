import json
import yaml
import tempfile
import unittest
import os

from probatus import loader

class TestLoadConfiguration(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.file_data = {"const1": "const2"}

    def test_load_json_file(self):
        _, fpath = tempfile.mkstemp(suffix=".json")
        with open(fpath, "w") as f:
            json.dump(self.file_data, f)
        result = loader.load_configuration(fpath)
        self.assertEqual(result, self.file_data)
        os.remove(fpath)

    def test_load_yaml_file(self):
        _, fpath = tempfile.mkstemp(suffix=".yml")
        with open(fpath, "w") as f:
            yaml.dump(self.file_data, f)
        result = loader.load_configuration(fpath)
        self.assertEqual(result, self.file_data)
        os.remove(fpath)

    def test_load_yaml_file_with_yaml_extension(self):
        _, fpath = tempfile.mkstemp(suffix=".yaml")
        with open(fpath, "w") as f:
            yaml.dump(self.file_data, f)
        result = loader.load_configuration(fpath)
        self.assertEqual(result, self.file_data)
        os.remove(fpath)

    def test_load_unsupported_file_format(self):
        _, fpath = tempfile.mkstemp(suffix=".txt")
        with open(fpath, "w") as f:
            f.write("text content that is not JSON or YAML")
        with self.assertRaises(ValueError):
            loader.load_configuration(fpath)
        os.remove(fpath)

if __name__ == '__main__':
    unittest.main()