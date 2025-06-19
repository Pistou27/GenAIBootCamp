import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

df_money_money = pd.read_csv(r'data_center\datascience_salaries.csv')
pd.set_option('display.max_columns', None)

# Vérification des duplicats
print(len(df_money_money))

df_money_money = df_money_money.drop_duplicates()

print(len(df_money_money))

# Sauvegarde de job_title avant suppression
df_money_money['job_title_original'] = df_money_money['job_title']

scaler = MinMaxScaler()
print(df_money_money['salary'].max())
df_money_money['salary'] = scaler.fit_transform(df_money_money[['salary']])

list_job_title = df_money_money['job_title'].unique()
list_job_type = df_money_money['job_type'].unique()
list_salary_currency = df_money_money['salary_currency'].unique()
list_job_titles = df_money_money['job_title'].unique()

experience_level_order = {'Entry': 0, 'Mid': 1, 'Senior': 2, 'Executive': 3}

le = LabelEncoder()
df_money_money['experience_level'] = df_money_money['experience_level'].map(experience_level_order)
df_money_money['job_type'] = le.fit_transform(df_money_money['job_type'])
df_money_money['salary_currency'] = le.fit_transform(df_money_money['salary_currency'])

df_dummies = pd.get_dummies(df_money_money['job_title'], prefix='exp')

df_money_money = pd.concat([df_money_money.drop('job_title', axis=1), df_dummies], axis=1)

# Affichage de la distribution des salaires normalisés par métier
plt.figure(figsize=(14, 7))
job_titles = df_money_money['job_title_original'].unique()

for title in job_titles:
    subset = df_money_money[df_money_money['job_title_original'] == title]
    plt.hist(subset['salary'], alpha=0.5, bins=20, label=title)

plt.title('Distribution des salaires normalisés par métier (toutes monnaies)')
plt.xlabel('Salaire normalisé')
plt.ylabel('Nombre d\'employés')
plt.legend(loc='upper right', fontsize='small')
plt.tight_layout()
plt.show()

print(df_money_money.head())

salary_stats = df_money_money.groupby('experience_level')['salary'].agg(['mean', 'median']).reset_index()
print(salary_stats)

"""
PCA mais illisible
numeric_cols = df_money_money.select_dtypes(include=['number']).columns

pca = PCA(n_components=2)
reduced_data = pca.fit_transform(df_money_money[numeric_cols])

reduced_df = pd.DataFrame(reduced_data, columns=['PC1', 'PC2'])

reduced_df.head()

plt.figure(figsize=(10, 6))
plt.scatter(reduced_df['PC1'], reduced_df['PC2'], alpha=0.5)
plt.title('PCA - Projection des données sur les deux premières composantes principales')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.grid(True)
plt.show()
"""

