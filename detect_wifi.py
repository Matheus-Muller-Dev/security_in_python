from wifi import Cell

interface = 'wlp2s0'

try:
    cells = Cell.all(interface)

    if not cells:
        print(f"Nenhuma rede wifi encontrada na interface {interface}.")
    else:
        cell_power = []

        for cell in cells:
            cell_power.append((cell.ssid, cell.signal))

            cell_power.sort(key=lambda cell_signal: cell_signal[1], reverse=True)

            print("Redes Wi-fi encontradas: ")
            for ssid, signal in cell_power:
                print(f"{ssid} - Sinal: {signal} dBm")

except Exception as e:
    print(f"Ocorreu um erro: {e}")