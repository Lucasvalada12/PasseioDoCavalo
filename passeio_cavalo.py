# passeio_cavalo.py

def passeio_do_cavalo(n, x_start=0, y_start=0, exibir_solucao=True):
    dx = [2, 1, -1, -2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]

    tabuleiro = [[0 for _ in range(n)] for _ in range(n)]

    def eh_valido(x, y):
        return 0 <= x < n and 0 <= y < n and tabuleiro[x][y] == 0

    def backtrack(i, x, y):
        if i > n * n:
            return True
        for m in range(8):
            xn, yn = x + dx[m], y + dy[m]
            if eh_valido(xn, yn):
                tabuleiro[xn][yn] = i
                if backtrack(i + 1, xn, yn):
                    return True
                tabuleiro[xn][yn] = 0
        return False

    tabuleiro[x_start][y_start] = 1
    if backtrack(2, x_start, y_start):
        if exibir_solucao:
            print("Solução encontrada:")
            for linha in tabuleiro:
                print(" ".join(f"{num:2}" for num in linha))
        return tabuleiro
    else:
        print("Não há solução.")
        return None
