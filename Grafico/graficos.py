import json
import matplotlib.pyplot as plt


class Graphic():
    def __init__(self, parent):
        super().__init__()

    def grafico(self):
        centro = ["La calera","Villa allende","Narnia"]
        personas = [0, 0, 0]
        file = "data.json"
        with open(file) as file:
            data = json.load(file)
            for persona in data:
                if persona["centro"] == "La calera":
                    personas[0] += 1
                if persona["centro"] == "Villa allende":
                    personas[1] += 1
                if persona["centro"] == "Narnia":
                    personas[2] += 1

        print(centro, personas)
        ejex = centro
        ejey = personas
        plt.bar(ejex, ejey)

        plt.ylabel("cantidad de vacunados")
        plt.xlabel("centro de vacunacion")
        plt.title("cantidad de vacunados por centros")

        plt.show()


