# Import necessary packages
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
import io
import re
import pandas as pd


# Reading the text from pdf using pdfminer library and storing data in list
def extract_text_from_pdf(pdf_file_name):
    """
    Reading text by looping through each page of the PDF and storing it in a list.

    Parameters:
        pdf_file_name: The location of the pdf file from which the text will be extracted
    Result:
        recipes (list): The list contains all the pdf's recipe data.
    """

    # Create a PDF resource manager object that stores shared resources
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    # Set parameters for analysis.
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    # Extract text
    fp = open(pdf_file_name, 'rb')
    page_no = 5
    recipes = []
    # Process each page contained in the document
    for pageNumber, page in enumerate(PDFPage.get_pages(fp)):
        if pageNumber == page_no:
            interpreter.process_page(page)
            # Get text from StringIO
            data = retstr.getvalue()
            recipes.append(data)
            data = ''
            retstr.truncate(0)
            retstr.seek(0)
            page_no += 1

    # Close all the file handles
    fp.close()
    device.close()
    retstr.close()
    return recipes


# Passing the pdf file path to the function
recipes = extract_text_from_pdf('/home/neosoft/Desktop/pdf_to_text/pizzeria_recipes.pdf')


def collecting_recipe_details(recipes):
    """
    By looping through each recipe, recipe data is
    divided into titles, ingredients, and procedures.

    Parameters:
        recipes (list): The list contains all of the pdf's recipe data.
    Result:
        recipes_titles (list): The list contains all  the recipes' names.
        recipes_ingredients (list): The list includes all  the recipes' ingredients.
        recipes_method (list): The list contains all  the recipes' procedures.
    """
    recipes_titles, recipes_ingredients, recipes_methods = [], [], []
    for i in range(len(recipes)):
        method = ""
        content_list = re.split("\n\n", recipes[i])
        recipes_titles.append(content_list[0].strip())
        ingredients_text = content_list[1].strip()
        ingredients_text = re.sub("\n", " ", ingredients_text)
        recipes_ingredients.append(ingredients_text)
        text = "FREE Cookbooks!! Stop Searching, Start Cooking!\nhttp://www.e−cookbooks.net"
        if content_list[-4] == text:
            paragraphs = content_list[2:-4]
        else:
            paragraphs = content_list[2:-3]
        for paragraph in paragraphs:
            paragraph = paragraph.strip()
            paragraph = re.sub("\n", " ", paragraph)
            method += paragraph + " "
        recipes_methods.append(method)
    return (recipes_titles, recipes_ingredients, recipes_methods)


recipes_titles, recipes_ingredients, recipes_methods = collecting_recipe_details(recipes)
csv_file_path = "/home/neosoft/Desktop/pdf_to_text/recipes.csv"


# Store recipe data to dataframe
recipe_df = pd.DataFrame()
recipe_df['Recipe'] = recipes_titles
recipe_df['Ingredients'] = recipes_ingredients
recipe_df['Procedure'] = recipes_methods
print(recipe_df)


# Save data to csv file
recipe_df.to_csv(csv_file_path, index=False)
