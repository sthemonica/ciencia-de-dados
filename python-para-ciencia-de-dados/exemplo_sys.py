import sys

if len(sys.argv) < 2:
    print("Informe seu nome ao rodar o programa")
    sys.exit()

print(f"Olá, {sys.argv[1]}!")