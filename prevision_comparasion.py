anos_teste = [5, 10]
for ano in anos_teste:
    salario_previsto = a * ano + b
    print(f"Para {ano} anos de experiência, o salário previsto é R$ {salario_previsto:.2f}")

y_pred = [a * xi + b for xi in anos]
y = salario

mae = sum(abs(yi - ypi) for yi, ypi in zip(y, y_pred)) / len(y)
print(f"Erro Médio Absoluto (MAE): {mae:.2f}")

model = LinearRegression()
model.fit(np.array(anos).reshape(-1, 1), np.array(salario))

print(f"Coeficiente a: {model.coef_[0]:.4f}")
print(f"Intercepto b: {model.intercept_:.4f}")
