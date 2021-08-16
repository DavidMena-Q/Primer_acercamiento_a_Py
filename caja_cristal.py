import unittest


def mayor_edad(edad):
    if edad >= 18:
        return True
    else:
        return False   


class PruebaDeCristalTest(unittest.TestCase):
    

    def test_mayor_edad(self):
        edad = 70

        resultado = mayor_edad(edad)

        self.assertEqual(resultado, True)

    def test_menor_edad(self):
        edad = 13

        resultado = mayor_edad(edad)

        self.assertEqual(resultado, False)



if __name__ == ('__main__'):
    unittest.main()
   