def linear_regression(x, y):
  if len(x) != len(y):
    print("Erro: As listas x e y devem ter o mesmo tamanho.")
  else:
    n = len(x)
    soma_x = sum(x)
    soma_y = sum(y)
    soma_xy = sum([x[i] * y[i] for i in range(n)])
    soma_x2 = sum([x[i] ** 2 for i in range(n)])

    a = (n * soma_xy - soma_x * soma_y) / (n * soma_x2 - soma_x ** 2)
    b = (soma_y - a * soma_x) / n

    print(f"Equação da reta: y = {a:.4f}x + {b:.4f}")

linear_regression(anos, salario)


def plot_regression(x, y, a, b):
    x_vals = list(x)
    y_preds = [a * xi + b for xi in x_vals]

    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, color='blue', label='Dados reais')
    plt.plot(x_vals, y_preds, color='red', label='Reta de regressão')
    plt.title('Regressão Linear - Salário vs Anos de Experiência')
    plt.xlabel('Anos de Experiência')
    plt.ylabel('Salário')
    plt.legend()
    plt.grid(True)
    plt.show()

a = 9449.9623
b = 25792.2002

plot_regression(anos, salario, a, b)

def estatistica(x, y, a, b):
    y_mean = sum(y) / len(y)

    y_pred = [a * xi + b for xi in x]

    ss_res = sum((yi - ypi) ** 2 for yi, ypi in zip(y, y_pred))

    ss_tot = sum((yi - y_mean) ** 2 for yi in y)

    r2 = 1 - (ss_res / ss_tot)
    return r2

r2 = estatistica(anos, salario, a, b)
print (f"Coeficiente de determinação (R²): {r2:.4f}")
