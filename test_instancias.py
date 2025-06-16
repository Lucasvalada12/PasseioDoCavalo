from src.passeio_cavalo import passeio_do_cavalo

def testar_instancias():
    for n in [1, 3, 5]:
        print(f"\nTeste com tabuleiro {n}x{n}:")
        passeio_do_cavalo(n)

if __name__ == "__main__":
    testar_instancias()
