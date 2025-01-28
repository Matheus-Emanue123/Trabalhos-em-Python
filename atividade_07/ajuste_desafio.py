import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def exponential_decay(t, A, k, C):
    return A * np.exp(-k * t) + C


np.random.seed(42) 
t = np.linspace(0, 10, 50) 
A_real, k_real, C_real = 5, 0.8, 1 
sigma = 0.5 
y_real = exponential_decay(t, A_real, k_real, C_real)
y_noisy = y_real + np.random.normal(0, sigma, size=t.shape) 

params_initial_guess = [1, 1, 1]
params_opt, params_cov = curve_fit(exponential_decay, t, y_noisy, p0=params_initial_guess)

A_est, k_est, C_est = params_opt

y_fit = exponential_decay(t, A_est, k_est, C_est)

errors = {
    "A": abs(A_est - A_real),
    "k": abs(k_est - k_real),
    "C": abs(C_est - C_real),
}

plt.figure(figsize=(10, 6))
plt.scatter(t, y_noisy, label="Dados experimentais (com ruído)", color="blue")
plt.plot(t, y_fit, label="Curva ajustada", color="red")
plt.plot(t, y_real, label="Curva real (sem ruído)", linestyle="dashed", color="green")
plt.xlabel("Tempo (s)")
plt.ylabel("y(t)")
plt.title("Ajuste de Curva de Decaimento Exponencial")
plt.legend()
plt.grid()
plt.show()

print("Erros absolutos médios:")
print(f"A: {errors['A']}")
print(f"k: {errors['k']}")
print(f"C: {errors['C']}")
