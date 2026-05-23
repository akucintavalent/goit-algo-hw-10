import scipy.integrate as spi
import random


def f(x):
    return -(x**2) + 4 * x + 3


def monte_carlo_integration(func, a, b, max_y, num_samples):
    total = 0
    for _ in range(num_samples):
        x = random.uniform(a, b)
        y = random.uniform(0, max_y)
        total += 1 if y <= func(x) else 0
    return total / num_samples * (b - a) * max_y


if __name__ == "__main__":
    result_scipy = spi.quad(f, 0, 5)[0]
    print("Scipy result:", result_scipy)
    result_monte_carlo = monte_carlo_integration(f, 0, 5, 7, 100000)
    print("Monte Carlo result:", result_monte_carlo)
    print("Difference:", abs(result_scipy - result_monte_carlo))
