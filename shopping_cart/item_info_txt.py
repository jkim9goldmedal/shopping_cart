def item_info(data,column):
    import pandas
    from pandas import DataFrame
    import unicodedata
    from tabulate import tabulate
    pandas.set_option('display.unicode.east_asian_width', True)
    df = pandas.DataFrame(data=data, columns=column)
    result = tabulate(df,df.columns,tablefmt = "github",showindex=False)
    return result
