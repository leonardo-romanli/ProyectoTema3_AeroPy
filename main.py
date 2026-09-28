import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons, Slider, TextBox

# ==========================================
# DATOS DE PARTIDA 
# ==========================================
voltaje_sensor = np.array([0.0, 1.25, 2.45, 3.80, 5.10])
fuerza_real = np.array([0.0, 15.2, 31.0, 48.5, 65.3])

matriz_estatica = np.array([
    [1.0, 1.0, 1.0],
    [0.0, 1.5, -1.5],
    [-2.0, 1.0, 1.0]
])
vector_cargas = np.array([25000.0, 1500.0, -800.0])

h_atm = np.array([0, 2000, 4000, 6000, 8000, 10000, 12000, 14000])
T_atm = np.array([288.15, 275.15, 262.15, 249.15, 236.15, 223.15, 216.65, 216.65])
P_atm = np.array([101325, 79501, 61660, 47217, 35651, 26499, 19399, 14170])

t_vuelo = np.linspace(0, 60, 1200)
v_vuelo = 800 * np.sin(np.pi * t_vuelo / 60) * np.exp(-0.02 * t_vuelo)

# ==========================================
# FUNCIONES 
# ==========================================

def apartado_1_balance_masas():
    # TODO: Persona 1
    # Usar np.linalg.solve
    pass

def apartado_2_calibracion_motor():
    # TODO: Persona 2
    # Usar np.polyfit
    pass

def apartado_3_perfil_atmosferico():
    # TODO: Persona 2
    # Usar np.interp
    pass

def apartado_4_regimen_transonico():
    # TODO: Persona 3
    # Búsqueda de raíces (sin bucles for)
    pass

def apartado_5_acelerometro_virtual():
    # TODO: Persona 3
    # Usar np.gradient
    pass

def apartado_6_altitud_apogeo():
    # TODO: Persona 4
    # Usar np.trapz
    pass

def crear_interfaz_grafica():
    # TODO:  Persona 5
    # Aquí irá la ventana única con los botones y sliders
    pass

if __name__ == "__main__":
    print("Iniciando Dashboard AeroPy-I...")
    # Aquí se llamarán a las funciones para probar