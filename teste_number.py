"""
Arquivo com tudo
"""
import multiplo

class TesteNumero:
    """
    Classe de teste do numero
    """
    def setup(self):
        """
        Função de setup
        """

    def test_multplo(self):
        """
        Função para testar o multiplo
        """
        resultado1 =  multiplo(10)
        print(resultado1)
        assert resultado1 == "Fizz"
