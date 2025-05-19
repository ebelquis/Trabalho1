class NaoEncontradoNaListaException(Exception):
    def __init__(self):
        super().__init__("Nao coseguimos encontrar na lista esse pametro")
