import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons, Slider
import matplotlib.image as mpimg

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

GAMMA = 1.4
R_AIRE = 287.0  # J/(kg·K)

# ==========================================
# FUNCIONES
# ==========================================

def apartado_4_regimen_transonico(mach_crítico):  #Cuando actualize el valor del slider la funcion usará ese valor
    h= 300*t_vuelo
    T = np.interp(h, h_atm, T_atm) #Interpolar, h_atm y T_atm se interpolan y dan 1200 valores de T para cada uno de los 1200 valores de h
    a=np.sqrt(T*GAMMA*R_AIRE)
    M= v_vuelo/a
    f= M - mach_crítico
    idx = np.where(np.diff(np.sign(f)) != 0)[0] #Esta linea transforma los valores de f en +1 y -1 , resta cada elemento del posterior y los que son distintos de 0 se añaden a idx
    if idx.size > 0:
        i = idx[0]
        t_c = t_vuelo[i] - f[i] * (t_vuelo[i+1] - t_vuelo[i]) / (f[i+1] - f[i])
        print(f"El cohete alcanza Mach {mach_crítico:.2f} en t = {t_c:.2f} s, "
              f"entrando en régimen supersónico/transónico.")
    else:
        t_c = None
        print(f"El cohete nunca alcanza Mach {mach_crítico:.2f} (máximo: {M.max():.2f}).")

    return t_vuelo, M, t_c
def apartado_5_acelerometro_virtual():
        pass

def crear_interfaz_grafica():
    plt.rcParams["font.family"] = "serif"
    plt.rcParams["font.serif"] = ["Times New Roman", "DejaVu Serif"]
    plt.rcParams["font.size"] = 10 
    fig = plt.figure(figsize=(12, 6))
    COLOR_FONDO = "#4495ff"      # azul oscuro (ventana)
    COLOR_PANEL = "#0e56b3"      # paneles
    COLOR_GRAFICA = "#d6e8ff"    # gráfica
    COLOR_TEXTO = "#000000"      # texto claro
    COLOR_ACENTO = "#ff4800"     # naranja cohete

    ax = fig.add_axes([0.35, 0.25, 0.6, 0.65])      # eje principal
    ax_radio = fig.add_axes([0.03, 0.4, 0.2, 0.4])  # panel izquierdo
    ax_slider = fig.add_axes([0.35, 0.08, 0.6, 0.04])
    fig.patch.set_facecolor(COLOR_FONDO)
    ax.set_facecolor(COLOR_GRAFICA)
    ax_slider.set_facecolor(COLOR_PANEL)
    ax_radio.set_facecolor(COLOR_PANEL)
    radio = RadioButtons(ax_radio, [f"Apartado {i}" for i in range(1, 7)])
    for etiqueta in radio.labels:
        etiqueta.set_color(COLOR_TEXTO)
        etiqueta.set_fontsize(11)

    slider = Slider(ax_slider, "Mach crítico", 0.8, 2.5, valinit=1.2,
                color=COLOR_ACENTO)
    slider.label.set_color(COLOR_TEXTO)
    slider.valtext.set_color(COLOR_TEXTO)
    plt.show()


if __name__ == "__main__":
    print("Iniciando Dashboard AeroPy-I...")
    crear_interfaz_grafica()
    #hola