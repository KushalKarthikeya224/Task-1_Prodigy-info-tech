import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Age': [15, 22, 35, 45, 51, 60, 18, 33, 40, 27, 19, 23, 37, 48, 55],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male', 
               'Female', 'Male', 'Female', 'Male', 'Female']
}

df = pd.DataFrame(data)

sns.set(style="whitegrid")

plt.figure(figsize=(6, 4))
sns.countplot(x='Gender', data=df, palette='Set2')
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 5))
sns.histplot(df['Age'], bins=6, kde=True, color='skyblue')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()