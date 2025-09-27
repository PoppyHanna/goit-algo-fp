import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

N = 100_000

cube1 = np.random.randint(1, 7, N)
cube2 = np.random.randint(1, 7, N)
sums = cube1 + cube2

unique, counts = np.unique(sums, return_counts=True)
probabilities = counts / N

analytic_probs = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36,
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36,
}

df = pd.DataFrame({
    "Sum": range(2, 13),
    "Monte-Carlo (%)": [round(probabilities[np.where(unique==s)][0]*100, 2) if s in unique else 0 for s in range(2, 13)],
    "Analitycal (%)": [round(analytic_probs[s]*100, 2) for s in range(2, 13)]
})

print(df)

plt.figure(figsize=(8,5))
plt.bar(df["Sum"]-0.2, df["Monte-Carlo (%)"], width=0.4, label="Monte-Carlo", alpha=0.7)
plt.bar(df["Sum"]-0.2, df["Analitycal (%)"], width=0.4, label="Analitycal", alpha=0.7)
plt.xlabel("Sum")
plt.ylabel("Probability (%)")
plt.title("Probabilities of sums when rolling two dice")
plt.xticks(range(2, 13))
plt.show()