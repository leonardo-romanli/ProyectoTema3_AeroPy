import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons, Slider

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

def apartado_4_regimen_transonico(t=t_vuelo, v=v_vuelo, M_crit=1.2, T_t=None):
    """Instantes t_c con M(t) = M_crit (cambios de signo + interpolación lineal)."""
    if T_t is None:
        T_t = np.interp(300.0 * t, h_atm, T_atm)   # T(t) del Apartado 3

    a = np.sqrt(GAMMA * R_AIRE * T_t)   # velocidad del sonido
    M = v / a                           # Mach
    g = M - M_crit

    idx = np.where((g[:-1] < 0) != (g[1:] < 0))[0]
    t_c = t[idx] - g[idx] * (t[idx + 1] - t[idx]) / (g[idx + 1] - g[idx])

    if t_c.size == 0:
        print(f"El cohete nunca alcanza Mach {M_crit:.2f} (Mach máximo = {M.max():.2f}).")
    else:
        lista = ", ".join(f"{x:.2f}" for x in t_c)
        print(f"El cohete cruza Mach {M_crit:.2f} en t = {lista} s: el primer cruce "
              f"es al acelerar y, si hay un segundo, al decelerar (Mach máx. {M.max():.2f}).")
    return t_c, M


def apartado_5_acelerometro_virtual(t=t_vuelo, v=v_vuelo):
    """a_long = dv/dt con diferencias finitas de 2.º orden."""
    a_long = np.gradient(v, t, edge_order=2)

    i_max, i_min = np.argmax(a_long), np.argmin(a_long)
    print(f"La aceleración máxima es {a_long[i_max]:.1f} m/s² "
          f"({a_long[i_max] / 9.81:.1f} g) en t = {t[i_max]:.2f} s; la máxima "
          f"deceleración es {a_long[i_min]:.1f} m/s² en t = {t[i_min]:.1f} s.")
    return a_long


def crear_interfaz_grafica():
    fig = plt.figure(figsize=(12, 6))

    ax = fig.add_axes([0.35, 0.25, 0.6, 0.65])      # eje principal
    ax_radio = fig.add_axes([0.03, 0.4, 0.2, 0.4])  # panel izquierdo
    ax_slider = fig.add_axes([0.35, 0.08, 0.5, 0.04])

    radio = RadioButtons(ax_radio, [f"Apartado {i}" for i in range(1, 7)])
    slider = Slider(ax_slider, "Mach crítico", 0.8, 2.5, valinit=1.2)

    def dibujar_4():
        t_c, M = apartado_4_regimen_transonico(M_crit=slider.val)
        ax.plot(t_vuelo, M, label="M(t)")
        ax.axhline(slider.val, color="r", ls="--", label=f"M = {slider.val:.2f}")
        ax.plot(t_c, np.full_like(t_c, slider.val), "ko")
        ax.set_xlabel("t [s]"); ax.set_ylabel("Mach"); ax.legend(loc="upper right")
        return "t_c = " + (", ".join(f"{x:.2f} s" for x in t_c) if t_c.size else "no existe")

    def dibujar_5():
        a = apartado_5_acelerometro_virtual()
        ax.plot(t_vuelo, a)
        ax.set_xlabel("t [s]"); ax.set_ylabel("a_long [m/s²]")
        return f"a_max = {a.max():.1f} m/s²"

    def pendiente():
        return "Apartado pendiente de implementar"

    paneles = {"Apartado 4": dibujar_4, "Apartado 5": dibujar_5}

    def actualizar(_=None):
        ax.clear()
        texto = paneles.get(radio.value_selected, pendiente)()
        ax.text(0.02, 0.95, texto, transform=ax.transAxes, va="top",
                bbox=dict(boxstyle="round", fc="white"))
        fig.canvas.draw_idle()

    radio.on_clicked(actualizar)
    slider.on_changed(actualizar)
    actualizar()
    plt.show()


if __name__ == "__main__":
    print("Iniciando Dashboard AeroPy-I...")
    crear_interfaz_grafica()
