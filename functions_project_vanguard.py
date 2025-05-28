# Funciones auxiliares
def overview(df):
    print(df.info())
    display(df.describe(include='all'))

def report_nulls_duplicates(df):
    print("Nulls por columna:", df.isnull().sum())
    print("Duplicados:", df.duplicated().sum())

def drop_duplicates(df):
    return df.drop_duplicates()

def drop_nulls(df):
    return df.dropna()

