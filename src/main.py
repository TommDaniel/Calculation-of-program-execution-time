import time
import csv
import matplotlib.pyplot as plt

from Fib_I import fib_i
from Fib_R import fib_r

def main():
    max_pos_iter = 100
    max_pos_rec_real = 30

    rec_times = []
    rec_values = []
    for pos in range(1, max_pos_rec_real + 1):
        start = time.perf_counter()
        value = fib_r(pos)
        end = time.perf_counter()
        rec_time = end - start

        rec_values.append(value)
        rec_times.append(rec_time)

    for pos in range(max_pos_rec_real + 1, max_pos_iter + 1):
        t_est = rec_times[pos - 2 - 1] + rec_times[pos - 3 - 1]
        rec_times.append(t_est)

        val_est = fib_i(pos)
        rec_values.append(val_est)

    iter_times = []
    iter_values = []
    for pos in range(1, max_pos_iter + 1):
        start = time.perf_counter()
        value = fib_i(pos)
        end = time.perf_counter()
        iter_time = end - start
        iter_times.append(iter_time)
        iter_values.append(value)

    with open("resultados_fibonacci.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerow(["Posicao",
                         "Valor",
                         "Tempo_Iterativo(seg)",
                         "Tempo_Recursivo(seg) (Real até 30, Estimado depois)"])

        for i in range(max_pos_iter):
            pos = i + 1
            valor = iter_values[i]
            t_iter = iter_times[i]

            t_rec = rec_times[i]

            writer.writerow([pos, valor, f"{t_iter:.6f}", f"{t_rec:.6f}"])

    print("Posicao;Valor;TempoIter;TempoRec(R=real até 30/E=estimado)")
    for i in range(max_pos_iter):
        pos = i + 1
        valor = iter_values[i]
        t_iter = iter_times[i]
        t_rec = rec_times[i]

        if pos <= max_pos_rec_real:
            tipo = "R"
        else:
            tipo = "E"

        print(f"{pos};{valor};{t_iter:.6f};{t_rec:.6f}({tipo})")

    import numpy as np

    posicoes = np.arange(1, max_pos_iter + 1)

    tempos_iter = np.array(iter_times)
    tempos_rec  = np.array(rec_times)

    plt.plot(posicoes, tempos_iter, label="Iterativo (real, 1..100)")
    plt.plot(posicoes, tempos_rec,  label="Recursivo (1..30 real, 31..100 estimado)")
    plt.xlabel("Posição na Série de Fibonacci")
    plt.ylabel("Tempo de Execução (segundos)")
    plt.title("Comparação de Tempos: Fibonacci Iterativo x Recursivo")
    plt.legend()

    # Salva em PNG
    plt.savefig("grafico_fibonacci.png", dpi=300)
    plt.show()


if __name__ == "__main__":
    main()
