
import matplotlib as plt
import seaborn as sns


_, axes = plt.subplots(1, 2, sharey=True, figsize=(10, 4))
   sns.set(rc={'figure.figsize': (16, 5)})


sns.boxplot(x='Outcome', y='BloodPressure', data=diabetes, ax=axes[0])


sns.violinplot(x='Outcome', y='BloodPressure', data=diabetes, ax=axes[1])

sns.boxplot(data=diabetes.select_dtypes(include='number'))


