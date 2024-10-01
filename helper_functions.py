def manage_outliers(dataframe):
    """
    This function takes a dataframe, sorts it by a specific column, and removes outliers.
    """        
    column_name = 'HH Income + Consumption + Assets + Residues / Day'
    dataframe = dataframe.sort_values([column_name])  
    dataframe["index"] = range(1, len(dataframe) + 1)  

    low = round(len(dataframe) * 0.01)
    upp = len(dataframe) - round(len(dataframe) * 0.04)
    
    dataframe['outlier'] = 0
    dataframe.loc[(dataframe['index'] > low) & (dataframe['index'] <= upp), 'outlier'] = 1
    
    # Filter the dataframe to keep only non-outliers
    dataframe = dataframe[dataframe['outlier'] == 1]
    
    return dataframe


def calculate_mean_median_by_status_ignoring_zeroes(data, column):
    """
    This calculates the mean and median by ignoring zeroes
    """
    return data[data[column] != 0].groupby('STATUS')[column].agg(['mean', 'median'])

def rename_columns(df, column_mappings):
    """
    rename columns passing in a mapping, of new and old namings. new column comes first
    """
    for new_col, old_col in column_mappings:
        df[new_col] = df[old_col]
