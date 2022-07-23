"""
Esse codigo simula o comportamento do aeropendulo em malha fechada com elementos do mundo real (perturbações e delay)
"""
# Importando bibliotecas
from scipy.integrate import odeint
from numpy import zeros, arange, pi, sin, sqrt, random
import matplotlib.pyplot as plt

# Definindo dinamica da planta
def din_aeropend(y, t, omega):
    # Parametros da planta
    b = 0.006856
    m = 0.3182
    g = 9.81
    I = 0.0264
    kh = 2.12829e-5
    Lh = 0.32

    # Definindo estados
    x1, x2 = y
    # Dinamica do pendulo
    x1p = x2
    x2p = (Lh*kh/I)*omega**2 - (Lh*m*g/I)*sin(x1) - (b/I)*x2
    return [x1p, x2p]


# Variaveis auxiliares
rad2deg = 180.0/pi
deg2rad = pi/180.0

# Parametros da planta
b = 0.006856
m = 0.3182
g = 9.81
I = 0.0264
kh = 2.12829e-5
Lh = 0.32

# Parametros de simulacao
Ta = 1e-3  # intervalo de amostragem
Tsim = 30  # tempo de simulacao
kend = int(Tsim/Ta)

# Scopes
omega = zeros(kend)  # rad/s
omega_delay = zeros(kend)  # rad/s
theta = zeros(kend)  # posicao angular
theta_ref = zeros(kend)  # referencia p/ posicao angular
erro = zeros(kend)  # erro de rastreamento
erro_int = zeros(kend)  # erro integral
thetap = zeros(kend)  # velocidade angular
n = zeros(kend)  # ruido de medida

# Valores de equilibrio
thetab = 30*deg2rad  # rad
omegab = sqrt(m*g*sin(thetab)/kh)

# Loop
for k in range(kend-1):

    # Referencia da planta
    if k*Ta > 1:
        theta_ref[k] = 15*deg2rad

    # Calculando erro de rastreamento
    erro[k] = theta_ref[k] - theta[k]
    erro_int[k] = erro_int[k-1] + erro[k]*Ta  # erro integral

    # Acao de controle (controlador PI+V)
    omega[k] = 70*erro[k] + 40*erro_int[k] - 50*thetap[k]

    # Saturacao
    omega[k] = min(omega[k], 375-omegab)  # sup
    omega[k] = max(omega[k], -omegab)  # inf

    # Atraso
    omega_delay[k] = omega[k - 100]

    # Evoluindo a din. da planta
    x0 = [theta[k] + thetab, thetap[k]]
    sol = odeint(din_aeropend, x0, [0.0, Ta], args=(omega_delay[k] + omegab,))
    n[k] = random.random(1)*(0.001 - (-0.001)) + (-0.001) #random from -0.1 to 0.001
    theta[k + 1] = sol[:, 0][-1] - thetab + n[k]
    thetap[k+1] = sol[:, 1][-1]


# Plotando resultados
fig1 = plt.figure()
plt.plot(arange(0, Tsim, Ta), (theta + thetab)*rad2deg, lw=2, label=r'$\theta$ (deg)')
plt.plot(arange(0, Tsim, Ta), (theta_ref + thetab)*rad2deg, 'r--', lw=2, label=r'$\theta_{ref}$ (deg)')
plt.xlabel('Tempo (s)')
plt.legend()
plt.grid(True)

fig2 = plt.figure()
plt.plot(arange(0, Tsim-Ta, Ta), omega_delay[0:-1] + omegab, 'r--', lw=2, label=r'$\omega$ (rad/s)')
plt.xlabel('Tempo (s)')
plt.legend()
plt.grid(True)

plt.show()
