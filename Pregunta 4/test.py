import tablas
import unittest
from io import StringIO
from unittest.mock import patch


class TestTableMethods(unittest.TestCase):
    #Test if a created class is an instance of clase
    def test_1(self):
        clase = "A f g h".split(" ")
        x = tablas.crear_clase(clase)
        self.assertIsInstance(x, tablas.Clase)
    #Test if a subclass is also instance of clase
    def test_2(self):
        clase = "B : A g k".split(" ")
        x = tablas.crear_clase(clase)
        self.assertIsInstance(x, tablas.Clase)
    #Test class with repeated methods
    def test_3(self):
        clase = "C a b k k".split(" ")
        with patch('sys.stdout', new=StringIO()) as mocked_stdout:
            tablas.crear_clase(clase)
            output = mocked_stdout.getvalue() 
        self.assertEqual(output, "Error, los metodos no deben estar repetidos en la declaración de la clase\n")

    #Create an already existing class
    def test_4(self):
        clase = "A a b".split(" ")
        with patch('sys.stdout', new=StringIO()) as mocked_stdout:
            tablas.crear_clase(clase)
            output = mocked_stdout.getvalue() 
        self.assertEqual(output, "La clase ya fue creada previamente, por favor introduzca otro nombre\n")
    #Describe a class with no heritage
    def test_5(self):
        describir = "A"

        with patch('sys.stdout', new=StringIO()) as mocked_stdout:
            tablas.initialize_describir(describir)
            output = mocked_stdout.getvalue() 
        self.assertEqual(output, "f -> A :: f\ng -> A :: g\nh -> A :: h\n")
    #Describe a class B with heritage
    def test_6(self):
        describir = "B"

        with patch('sys.stdout', new=StringIO()) as mocked_stdout:
            tablas.initialize_describir(describir)
            output = mocked_stdout.getvalue() 
        self.assertEqual(output, "f -> A :: f\ng -> B :: g\nh -> A :: h\nk -> B :: k\n")

    def test_7(self):
        entrada = "CLASS G : B n m h\nSALIR\n"
        with patch('sys.stdin', StringIO(entrada)) as mocked_stdin:
            with patch('sys.stdout', new=StringIO()) as mocked_stdout:
                tablas.main()
                output = mocked_stdout.getvalue()                
                expected_output = "Clase G creada con éxito"
                
                self.assertTrue(expected_output in output)
    #Test menu describir functionality
    def test_8(self):
        entrada = "DESCRIBIR G\nSALIR\n"
        with patch('sys.stdin', StringIO(entrada)) as mocked_stdin:
            with patch('sys.stdout', new=StringIO()) as mocked_stdout:
                tablas.main()
                output = mocked_stdout.getvalue()                
                expected_output = "f -> A :: f\ng -> B :: g\nh -> G :: h\nk -> B :: k\nn -> G :: n\nm -> G :: m\n"
        
                self.assertTrue(expected_output in output)

if __name__ == '__main__':
    unittest.main()
