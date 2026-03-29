
def inventory_checker():
    for i in range(0,min(len(df2.index), len(df1.index))):
        try:
            if df1.loc[i,'Column A'] != df2.loc[i,'Column A']:
                if df2.loc[i,'Column A'] not in df1.loc[:,'Column A'].values:
                    difference_list2.append(df2.loc[i,'Column A'])
                    n = n + 1
                    df2.drop([i],inplace = True)
                elif df1.loc[i,'Column A'] not in df2.loc[:,'Column A'].values:
                    difference_list1.append(df1.loc[i,'Column A'])
                    m = m + 1
                    df1.drop([i],inplace = True)
        except (IndexError, KeyError) as error:
            pass
