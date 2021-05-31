import pytest

import multiplo

class testenumero:
    def setup(self):
        pass

    def test_multplo(self):
        resultado1 =  multiplo(10)
        print(resultado1)
        
        assert resultado1 == "Fizz"
