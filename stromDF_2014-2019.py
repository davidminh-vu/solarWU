import pandas as pd

# Dateiname und Pfad zum CSV-Datenset
filename = 'strom2014-2019.csv'
# Lesen Sie das CSV-Datenset und geben Sie die erforderlichen Optionen an
df = pd.read_csv(filename, delimiter=';', parse_dates=['Intervall'], dayfirst=True, thousands=' ', usecols=['Intervall', 'StromKW'])

# Entfernen Sie die leere Spalte
df.dropna(axis=1, inplace=True)

# Erstellen Sie separate Spalten für Jahr, Monat und Tag
df['Jahr'] = df['Intervall'].dt.year
df['Monat'] = df['Intervall'].dt.month
df['Tag'] = df['Intervall'].dt.day

# Ändern Sie den Namen der 'StromKW' Spalte in 'Strom' und konvertieren Sie sie in eine Fließkommazahl
df.rename(columns={'StromKW': 'Strom'}, inplace=True)
df['Strom'] = df['Strom'].str.replace(' ', '').str.replace(',', '.').astype(float)

# Reihenfolge der Spalten anpassen
df = df[['Jahr', 'Monat', 'Tag', 'Strom']]

t=df[df['Jahr'] == 2019]['Strom'].sum()
print(t)
