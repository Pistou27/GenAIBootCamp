import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)

# Exercise 1: Duplicate Detection and Removal
titanic_data = pd.read_csv(r'data_center\train.csv')

# Verification de la taille du data frame
#print(len(titanic_data))

duplicates = titanic_data.head(5)
titanic_data = pd.concat([titanic_data, duplicates], ignore_index=True)

#Normalement titanic_data + 5
#print(len(titanic_data))

titanic_data = titanic_data.drop_duplicates()

#print(titanic_data.duplicated().sum())



# Exercise 2: Handling Missing Values

#Question 1
missing_data = titanic_data.isnull()
#print(missing_data.sum())

#Question 2
#Traitment numerical,                categorial,                                      low-utility (or heavy missing) or any type
#Imputation with the mean or median, Imputation with the most frequent value (mode), Drop the column,                   Drop rows with missing values (if few)

#Question 3
titanic_data["Age"].fillna(titanic_data["Age"].mean(), inplace=True)

titanic_data["Embarked"].fillna(titanic_data["Embarked"].mode()[0], inplace=True)

titanic_data.drop(columns=["Cabin"], inplace=True)

missing_data2 = titanic_data.isnull()

#print(missing_data2.sum())


# Exercise 3: Feature Engineering
print(titanic_data.info())
# print(titanic_data.head())

titanic_data["Title"] = titanic_data["Name"]
titanic_data.drop(columns=["Name"], inplace=True)

titanic_data["Family Size"] = titanic_data["SibSp"] + titanic_data["Parch"] + 1
titanic_data.drop(columns=["SibSp", "Parch"], inplace=True)

le = LabelEncoder()
titanic_data['Sex'] = le.fit_transform(titanic_data['Sex'])
titanic_data['Embarked'] = le.fit_transform(titanic_data['Embarked'])

#print(titanic_data.head())

# Exercise 4: Outlier Detection and Handling

def detect_outliner(columns, df_data):
    Q1 = df_data[columns].quantile(0.25)
    Q3 = df_data[columns].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df_data[(df_data[columns] >= lower_bound) & (df_data[columns] <= upper_bound)]
titanic_data = detect_outliner('Fare', titanic_data)
titanic_data = detect_outliner('Age', titanic_data)

# Exercise 5: Data Standardization and Normalization

scaler = MinMaxScaler()
titanic_data['Age'] = scaler.fit_transform(titanic_data[['Age']])
titanic_data['Fare'] = scaler.fit_transform(titanic_data[['Fare']])
#print(titanic_data.head())

# Exercise 6: Feature Encoding Fait dans le 3

# Exercise 7: Data Transformation for Age Feature

bins = [0, 0.12, 0.18, 0.60, 1.0]
cat = ['Child', 'Teen', 'Adult', 'Senior']

titanic_data['Age Group'] = pd.cut(titanic_data['Age'], bins=bins, labels=cat)

age_dummies = pd.get_dummies(titanic_data['Age Group'], prefix='AgeGroup')
titanic_data = pd.concat([titanic_data, age_dummies], axis=1)

print(titanic_data.head())

# Compter le nombre de passagers par groupe d'âge
age_group_counts = titanic_data['Age Group'].value_counts().sort_index()

# Création du graphique
plt.figure(figsize=(8, 5))
age_group_counts.plot(kind='bar', color='skyblue', edgecolor='black')

# Personnalisation
plt.title('Répartition des passagers par groupe d\'âge')
plt.xlabel('Groupe d\'âge')
plt.ylabel('Nombre de passagers')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Affichage
plt.tight_layout()
plt.show()