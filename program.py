import math

# Constants
G = 6.6743e-11  # gravitational constant, m^3/kg/s^2
M_sun = 1.9891e30  # mass of the Sun, kg
M_jup = 1.898e27  # mass of Jupiter, kg

# Get input from user
m_star = float(input("Введите массу звезды (в солнечных массах): ")) * M_sun
period = float(input("Введите период обращения планеты (в днях): ")) * 86400  # convert to seconds
semi_major_axis = float(input("Введите большую полуось планеты (в а.е.): ")) * 1.496e11  # convert to meters
eccentricity = float(input("Введите эксцентриситет планеты: "))
inclination = math.radians(float(input("Введите наклон планеты (в градусах): ")))
m_planet = float(input("Введите массу планеты (в массах Юпитера): ")) * M_jup
t = float(input("Введите время (в секундах): "))
t0 = float(input("Введите время, в которое планета находилась в исходном положении (в секундах): "))
omega = float(input("Введите долготу периастра (в радианах): "))

# Calculate radial velocity
K = 2 * math.pi * G**(1/3) * m_planet * math.sin(inclination) / ((m_star + m_planet)**(2/3) * math.sqrt(G * m_star) * math.sqrt(1 - eccentricity**2))
v_rad = K * math.cos(inclination) * (math.cos(2 * math.pi * (t - t0) / period) + eccentricity * math.cos(omega))

# Print result
print(f"Лучевая скорость звезды равна ", v_rad, "m/s.")
