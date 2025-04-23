def exchange_money(budget, exchange_rate):
    if exchange_rate <= 0:
        return "Error"
    return round(budget / exchange_rate, 2)

exchange_rates = {
    "japon": 0.0071,
    "mexico": 0.051,
    "francia": 1.14,
    "bolivia": 0.14
}

print("=== Calculadora de Divisas ===")
print("Países: Japon, Mexico, Francia, Bolivia")

pais = ""
while pais not in exchange_rates:
    pais = input("Elija un país: ").strip().lower()
    if pais not in exchange_rates:
        print("País no disponible. Intente de nuevo.")

try:
    presupuesto = float(input("Presupuesto en USD: "))
    if presupuesto <= 0:
        print("Error")
    else:
        tasa = exchange_rates[pais]
        resultado = exchange_money(presupuesto, tasa)
        print(f"{presupuesto} USD equivale a {resultado} en {pais.title()}.")
except ValueError:
    print("Error")
