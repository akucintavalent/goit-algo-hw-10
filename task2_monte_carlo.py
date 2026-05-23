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
    random.seed(42)

    a = 0
    b = 4.5
    max_y = 7
    num_samples = 100000

    result_scipy, error = spi.quad(f, a, b)
    result_analytical = -(b**3 - a**3) / 3 + 2 * (b**2 - a**2) + 3 * (b - a)
    result_monte_carlo = monte_carlo_integration(f, a, b, max_y, num_samples)

    print("Analytical result:", result_analytical)
    print("Scipy result:", result_scipy)
    print("Scipy absolute error estimate:", error)
    print("Monte Carlo result:", result_monte_carlo)
    print("Difference:", abs(result_scipy - result_monte_carlo))
