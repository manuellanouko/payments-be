import pandas
import pathlib

FILE_SUB_PATH = "data/static/payment_information.csv"
FILE_PATH = str(pathlib.Path(__file__).absolute().parent.parent / FILE_SUB_PATH)

def normalise_payments_data():
    try:
        dataframe: pandas.DataFrame = pandas.read_csv(FILE_PATH)
        dataframe["total_due"] = 0.0
        return dataframe
    except Exception as e:
        print(e)
