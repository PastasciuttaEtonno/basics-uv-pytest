from operazioni import *

def calcolatrice(operazione:str, a:float, b:float):
    if operazione == "somma":
        return somma(a, b)
    elif operazione == "sottrazione":
        return sottrazione(a, b)
    elif operazione == "moltiplicazione":
        return moltiplicazione(a, b)
    elif operazione == "divisione":
        return divisione(a, b)
    else:
        return "Operazione non valida"


def main(): 
    print(calcolatrice("somma", 2, 3))
    print(calcolatrice("sottrazione", 5, 3))


if __name__ == "__main__":
    main()