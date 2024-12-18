import json
import socket
import time
import PiMotor
import RPi.GPIO as GPIO

if __name__ == '__main__':

    levyMotor = PiMotor.Motor("MOTOR1", 1)
    pravyMotor = PiMotor.Motor("MOTOR2", 1)
    sipkaVzad = PiMotor.Arrow(1)
    sipkaVlevo = PiMotor.Arrow(2)
    sipkaVpred = PiMotor.Arrow(3)
    sipkaVpravo = PiMotor.Arrow(4)
    obaMotory = PiMotor.LinkedMotors(pravyMotor, levyMotor)

    klic = ""
    ipina = "10.42.0.1"
    port = 5005
    prihlport = port + 20

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ipina, port))

    bsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bsock.bind((ipina, prihlport))

    while True:
        bdata, addr = bsock.recvfrom(1024)
        klic = bdata.decode('utf-8')

        while True:
            data, addr = sock.recvfrom(1024)
            decoded_data = data.decode('utf-8')
            json_data = json.loads(decoded_data)
            smer_jizdy = json_data["smerJizdy"]
            autentifikace = json_data["autentifikace"]
            print(f"received message: {data}")

            if klic == autentifikace:

                if smer_jizdy == "87":
                    print("Vpřed")
                    sipkaVpred.on()
                    sipkaVzad.off()
                    sipkaVlevo.off()
                    sipkaVpravo.off()
                    obaMotory.forward(100)
                    time.sleep(0.03)
                    obaMotory.stop()
                    sipkaVpred.off()
                elif smer_jizdy == "65":
                    print("otoc vlevo")
                    sipkaVpred.off()
                    sipkaVzad.off()
                    sipkaVlevo.on()
                    sipkaVpravo.off()
                    levyMotor.reverse(100)
                    pravyMotor.forward(100)
                    time.sleep(0.03)
                    levyMotor.stop()
                    pravyMotor.stop()
                    sipkaVlevo.off()
                elif smer_jizdy == "83":
                    print("Vzad")
                    sipkaVpred.off()
                    sipkaVzad.on()
                    sipkaVlevo.off()
                    sipkaVpravo.off()
                    obaMotory.reverse(100)
                    time.sleep(0.03)
                    obaMotory.stop()
                    sipkaVzad.off()
                elif smer_jizdy == "68":
                    print("otoc vpravo")
                    sipkaVpred.off()
                    sipkaVzad.off()
                    sipkaVlevo.off()
                    sipkaVpravo.on()
                    levyMotor.forward(100)
                    pravyMotor.reverse(100)
                    time.sleep(0.03)
                    levyMotor.stop()
                    pravyMotor.stop()
                    sipkaVpravo.off()

                elif smer_jizdy == "81":
                    print("Vpred vlevo")
                    sipkaVpred.on()
                    sipkaVzad.off()
                    sipkaVlevo.on()
                    sipkaVpravo.off()
                    levyMotor.forward(0)
                    pravyMotor.forward(100)
                    time.sleep(0.03)
                    levyMotor.stop()
                    pravyMotor.stop()
                    sipkaVlevo.off()
                    sipkaVpred.off()

                elif smer_jizdy == "69":
                    print("Vpred vpravo")
                    sipkaVpred.on()
                    sipkaVzad.off()
                    sipkaVlevo.off()
                    sipkaVpravo.on()
                    levyMotor.forward(100)
                    pravyMotor.forward(0)
                    time.sleep(0.03)
                    levyMotor.stop()
                    pravyMotor.stop()
                    sipkaVpravo.off()
                    sipkaVpred.off()

                elif smer_jizdy == "27":
                    klic = ""
                    break
