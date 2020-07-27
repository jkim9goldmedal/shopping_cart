def item_info(data,column):
    import pandas
    from pandas import DataFrame
    import unicodedata
    from tabulate import tabulate
    """
    tabuate.WIDE_CHARS_MODE = False
    """
    df = pandas.DataFrame(data=data, columns=column)
    result = tabulate(df,df.columns,tablefmt = "github",showindex=False)
    return result
