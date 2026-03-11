import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

sns.scatterplot(
    x="total_bill",
    y="tip",
    hue="sex",        # color
    size="size",      # size of dots
    data=df
)
# this is a nothing.
plt.show()