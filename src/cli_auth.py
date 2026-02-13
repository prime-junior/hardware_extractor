import streamlit as st
import pandas as pd
import re
from utils import open_gsheet, extract_update_cell


try:
    # Call the function to get a worksheet.
    worksheet = open_gsheet() 

    def create_df(worksheet):
        """Returns a pandas format dataframe.
         
        With the format from pandas library from the gspread.worksheet.Worksheet data type
        obtained with the function open_gsheet(). Then, pandas DataFrame method converts
        gspread.worksheet.Worksheet to readable data.

        Argument:
            worksheet (gspread.worksheet.Worksheet): When using the Google Cloud credentials to access a spresheet,
            the function open_gsheet() returns the first sheet as gspread.worksheet.Worksheet data type. 

        Return: 
            pandas.core.frame.DataFrame: Returns a dataframe with the format from pandas library from the gspread.worksheet.Worksheet data type
            obtained with the function open_gsheet().
        """
        return pd.DataFrame(worksheet.get_all_records())
    
    df = create_df(worksheet)

    def part_number_input():
        """Returns a text area on the browser to input the part number to be extracted.
        The inputted part number is stored under the variable part_number."""
        part_number = st.text_input("Part Number: ") 
        return part_number

    part_number = part_number_input()

    def button_to_input_part_number(part_number):
        """Returns a button on the browser to run the application and update the browser.
        Returns a regex pattern on the back-end.

        As soon as the button is pressed, the part number inputted on the text area
        is stored under the variable part_number. The part_number inputted becomes a regex pattern,
        so that the part number inputted along with its variations can be extracted from the column 'OLD PART NUMBER(S)'.

        Arguments: 
            part_number (str): The string inputted on the text area on the browser.

        Return: 
            regex: Pattern after adding the part number inputted + regex. The regex are used to extract the part inputted
            along with its variations. For example:

            inputted part number: 1234

            extracted part numbers: 1234AA, 1234AB, 1234AC    
        """
        if st.button("Part Number Input"):
            if len(part_number) < 8 :
                st.write("Please, enter the correct part number.")
            else:
                pattern = fr'((?:\n)?{re.escape(part_number)}[^\s]*)'

        return pattern

    pattern = button_to_input_part_number(part_number)

    # Condition when button is pressed
    if pattern:
        extract_update_cell(df, pattern, worksheet)

    worksheet_updated = open_gsheet()

    df_updated = create_df(worksheet_updated)

except Exception as e:
    print(f'Error: {e}')


# streamlit run cli_auth.py