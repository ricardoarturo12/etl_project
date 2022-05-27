
import pandas as pd
from pip import main
import sqlalchemy

FILE_XLS = "consolidado.xlsx"
FILE_PATH = "data/data1.sqlite3"

def format_data(df, columns_name):
    """Strip and capitalize columns data

    Args:
        df (dataframe): dataframe
        columns_name (list): columns
    """
    for col_name in columns_name:
        df[col_name] = df[col_name].str.strip()
        df[col_name] = df[col_name].str.capitalize()


def extract():
    # engine = sqlalchemy.create_engine(f'sqlite:///{FILE_PATH}')
    engine = sqlalchemy.create_engine("postgresql://admin:12345@127.0.0.1:5455/consolidado?sslmode=prefer")
    df = pd.read_excel(io=FILE_XLS, sheet_name="Consolidado")
    return engine, df


def transform(df):
    df = df.convert_dtypes()
    df.columns = [x.strip() for x in df.columns]
    columns_name = ['Tipo', 'País', 'Analista', 'Estado']
    format_data(df, columns_name)
    df['Compañía'] = df['Compañía'].str.strip()
    df['Compañía'] = df['Compañía'].str.upper()
    df['Fecha de alta'] = pd.to_datetime(df['Fecha de alta'],  errors='coerce')
    df['% de Avance'] = pd.to_numeric(df['% de Avance'], errors='coerce')

    return df


def load(df, engine):
    with engine.connect() as connection:
        df.to_sql(
            name="consolidado",
            con=connection,
            if_exists="replace",
        )
    connection.close()


def main():
    engine, df = extract()

    df = transform(df)

    load(df, engine)


if __name__ == "__main__":
    main()