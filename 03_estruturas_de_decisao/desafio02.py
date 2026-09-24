faturamento = float(input("Informe o faturamento anual: "))

if faturamento <= 50000:
    taxa = faturamento * 0.05
elif faturamento <= 100000:
    taxa = faturamento * 0.10
else:
    taxa = faturamento * 0.15

print(f"Faturamento: R$ {faturamento:.2f}")
print(f"Taxa comercial: R$ {taxa:.2f}")