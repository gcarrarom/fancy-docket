import unittest
from fancydocket import fancydocket
from click.testing import CliRunner

class FancyDocketTests(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(FancyDocketTests, self).__init__(*args, **kwargs)
    
    def test_path_to_file(self):
        proper_model = """
            This is a proper model that says hello to {name of the person}
        """
        runner = CliRunner()

        with runner.isolated_filesystem():
            with open('proper_model.txt', 'w') as filewriter:
                filewriter.write(proper_model)

            with open('proper_model.txt', 'r') as filereader:
                something = filereader.read()

            result = runner.invoke(fancydocket, ['--path', './proper_model.txt'], input='Guilherme')

        self.assertEqual(result.exit_code, 0)
        results = [output.strip() for output in result.output.split('\n')]
        self.assertTrue(results[0] == 'name of the person: Guilherme')
        self.assertTrue('This is a proper model that says hello to Guilherme' in results)

    def test_path_to_file_with_international_characters(self):
        proper_model = """
            Andréa says Hello to Antônio, çéüzs {namé of the perçsön}.... LOL
        """
        runner = CliRunner()

        with runner.isolated_filesystem():
            with open('proper_model.txt', 'w') as filewriter:
                filewriter.write(proper_model)

            with open('proper_model.txt', 'r') as filereader:
                something = filereader.read()

            result = runner.invoke(fancydocket, ['--path', './proper_model.txt'], input='Gui Martins')

        self.assertEqual(result.exit_code, 0)
        results = [output.strip() for output in result.output.split('\n')]
        self.assertTrue(results[0] == 'namé of the perçsön: Gui Martins')
        self.assertTrue('Andréa says Hello to Antônio, çéüzs Gui Martins.... LOL' in results)


if __name__ == '__main__':
    unittest.main()