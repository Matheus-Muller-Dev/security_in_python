from pywifi import PyWiFi, const, Profile
import time

# Inicializa o PyWiFi e a interface de rede
wifi = PyWiFi()
iface = wifi.interfaces()[0]  # Obtém a primeira interface de Wi-Fi

# Realiza a varredura para redes Wi-Fi
iface.scan()
time.sleep(2)  # Aguarda 2 segundos para a varredura

# Obtém os resultados da varredura
networks = iface.scan_results()

# Ordena as redes pelo nível de sinal (em dBm)
networks.sort(key=lambda network: network.signal, reverse=True)

# Exibe as redes Wi-Fi com o nível de sinal
print("Redes Wi-Fi encontradas:")
for network in networks:
    print(f"{network.ssid} - Sinal: {network.signal} dBm")
