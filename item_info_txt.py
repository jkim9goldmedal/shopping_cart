def item_info(data,column):
    import pandas
    from pandas import DataFrame
    import unicodedata
    from tabulate import tabulate
    df = pandas.DataFrame(data=data, columns=column)
    result = tabulate(df, df.columns,tablefmt = "github",showindex=False)
    return result
