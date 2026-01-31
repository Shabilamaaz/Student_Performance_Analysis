import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("students.csv")

print("Dataset shape:", df.shape)
print("\nColumns:\n", df.columns)
print("\nFirst 5 rows:\n", df.head())

print("\nBasic Info:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

import matplotlib.pyplot as plt
import seaborn as sns

sns.countplot(x='sex', data=df)
plt.title("Gender Distribution of Students")
plt.show()

print("\nSummary Statistics (Marks):")
print(df[['G1', 'G2', 'G3']].describe())

# Pass / Fail column
df['result'] = df['G3'].apply(lambda x: 'Pass' if x >= 10 else 'Fail')

print("\nPass / Fail Count:")
print(df['result'].value_counts())

plt.figure()
sns.countplot(x='result', data=df)
plt.title("Pass vs Fail Distribution")
plt.xlabel("Result")
plt.ylabel("Number of Students")
plt.show()

plt.figure()
sns.scatterplot(x='absences', y='G3', data=df)
plt.title("Absences vs Final Grade")
plt.xlabel("Number of Absences")
plt.ylabel("Final Grade (G3)")
plt.show()

plt.figure()
sns.countplot(x='studytime', hue='result', data=df)
plt.title("Study Time vs Pass/Fail")
plt.xlabel("Study Time")
plt.ylabel("Number of Students")
plt.show()
