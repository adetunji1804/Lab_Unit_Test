from unittest import TestCase #imported module
import camelCase #imported module

class TestCamelCase(TestCase): # Test Claas
    def test_right_sentence_ouput(self):
        input_and_expected_outputs ={ # dictiobary list with key value pair of test sentences or input and camelcase output
            '' : '',
            'hello' : 'hello', 'Hello' : 'hello', 'Hello world' : 'helloWorld',
            'HELLO WORLD' : 'helloWorld', 'hELLO wORLD' : 'helloWorld',
            'This is a  sentence' : 'thisIsASentence',
            'Spaces Before' : 'spacesBefore', 'Spaces  Every  where': 'spacesEveryWhere',
            'There is a }% tab here' : 'invalid character included'
                }
        for input_val in input_and_expected_outputs.keys(): #iterate through dictionary key of the list
                # assertEqual(expected, user_input)
            self.assertEqual(input_and_expected_outputs[input_val], camelCase.camelCase(input_val))