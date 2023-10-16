def data_extraction():
    input_df
    df1 = file_type_extraction(input_df) # abhishek
    df2 = direct_extraction(input_df) # prakhar
    final_df = pd.concat([df1, df2], ignore_index=True)
    return final_df


def main():
    df = data_extraction() #abhishek
    df = data_manipulation(df) #prakhar
    touch_excel(df)