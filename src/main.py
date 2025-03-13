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

    with open("fibonacci_results.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerow(["Position",
                         "Value",
                         "Iterative_Time(sec)",
                         "Recursive_Time(sec) (Real up to 30, Estimated after)"])

        for i in range(max_pos_iter):
            pos = i + 1
            value = iter_values[i]
            t_iter = iter_times[i]

            t_rec = rec_times[i]

            writer.writerow([pos, value, f"{t_iter:.6f}", f"{t_rec:.6f}"])

    print("Position;Value;IterTime;RecTime(R=real up to 30/E=estimated)")
    for i in range(max_pos_iter):
        pos = i + 1
        value = iter_values[i]
        t_iter = iter_times[i]
        t_rec = rec_times[i]

        if pos <= max_pos_rec_real:
            tipo = "R"
        else:
            tipo = "E"

        print(f"{pos};{value};{t_iter:.6f};{t_rec:.6f}({tipo})")

    import numpy as np

    positions = np.arange(1, max_pos_iter + 1)

    iter_times_np = np.array(iter_times)
    rec_times_np = np.array(rec_times)

    plt.plot(positions, iter_times_np, label="Iterative (real, 1..100)")
    plt.plot(positions, rec_times_np, label="Recursive (1..30 real, 31..100 estimated)")
    plt.xlabel("Position in the Fibonacci Series")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Time Comparison: Iterative vs Recursive Fibonacci")
    plt.legend()

    # Save as PNG
    plt.savefig("fibonacci_chart.png", dpi=300)
    plt.show()


if __name__ == "__main__":
    main()
