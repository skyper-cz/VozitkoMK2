import json
import socket

if __name__ == '__main__':
    ipina = "127.0.0.1"
    port = 5005

    # Nastavení UDP socketu
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ipina, port))

    print(f"Server běží na {ipina}:{port} a čeká na zprávy...")

    while True:
        # Přijímání zpráv
        data, addr = sock.recvfrom(1024)  # Velikost bufferu: 1024 bajtů
        try:
            # Zpracování dat
            decoded_data = data.decode('utf-8')  # Převod z bajtů na string
            json_data = json.loads(decoded_data)  # Načtení JSON
            smer_jizdy = json_data.get("smerJizdy", "Neznámé")
            autentifikace = json_data.get("autentifikace", "Neznámé")

            # Výpis přijaté zprávy
            print(f"Přijatá zpráva: {decoded_data}")
            print(f"Směr jízdy: {smer_jizdy}, Autentifikace: {autentifikace}")
        except json.JSONDecodeError:
            print(f"Chyba při dekódování JSON: {data}")
        except Exception as e:
            print(f"Neočekávaná chyba: {e}")