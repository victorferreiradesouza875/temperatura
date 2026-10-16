# 🌡️ Monitor de Temperatura do Laboratório

Script simples em Python, executado no terminal, que recebe uma temperatura digitada pelo usuário e exibe uma mensagem indicando a condição do ambiente e a ação recomendada.

## ✨ Funcionalidades

- Lê a temperatura informada pelo usuário (aceita números decimais)
- Classifica a temperatura em quatro faixas
- Exibe um alerta ou recomendação de acordo com a faixa

## 🛠️ Requisitos

- Python 3.6 ou superior
- Nenhuma biblioteca externa

## ▶️ Como executar

```bash
python temperatura.py
```

> Substitua `temperatura.py` pelo nome que você deu ao arquivo.

## 📋 Regras de classificação

| Temperatura | Mensagem exibida |
|---|---|
| Exatamente `0` | Temperatura baixa, cuidado com o congelamento. |
| Até `15` (exceto 0) | Frio intenso no laboratorio. |
| De `15` (exclusivo) até `25` | Temperatura agradável. |
| Acima de `25` | Temperatura alta! Ligar sistema de refrigeração. |

## 💻 Exemplos de uso

```
Digite a temperatura: 0
Temperatura baixa, cuidado com o congelamento.
```

```
Digite a temperatura: 10
Frio intenso no laboratorio.
```

```
Digite a temperatura: 22.5
Temperatura agradável.
```

```
Digite a temperatura: 30
Temperatura alta! Ligar sistema de refrigeração.
```

## ⚠️ Observações e limitações

- Se o usuário digitar algo que não seja um número (por exemplo, `abc`), o programa encerra com `ValueError`, pois a entrada não é validada.
- A primeira condição só é verdadeira para o valor exato `0`. Temperaturas negativas (como `-5`) caem na faixa "Frio intenso", e não na mensagem de congelamento. Se a intenção for alertar para congelamento em qualquer valor igual ou abaixo de zero, a condição pode ser trocada por `temperatura <= 0`.
- O programa avalia uma única temperatura e termina; não há repetição.
- A unidade não é especificada no código, mas as faixas sugerem graus Celsius (°C).

## 🚀 Ideias de melhorias

- Tratar entradas inválidas com `try/except`
- Ajustar a condição de congelamento para `temperatura <= 0`
- Permitir várias leituras seguidas com um laço `while`
- Registrar as leituras e alertas em um arquivo de log

## 📄 Licença

Livre para uso educacional e modificação.
