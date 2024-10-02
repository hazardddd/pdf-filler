import re
import PyPDF2
from PyPDF2 import PdfReader, PdfWriter

def load_data_from_text(file_path):
    """Reads the data from dummy_data.txt and returns it as a dictionary."""
    data = {}
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        # Define a helper function to safely extract data
        def extract_field(pattern, content, field_name):
            match = re.search(pattern, content)
            if match:
                return match.group(1).strip()
            else:
                print(f"Warning: Field '{field_name}' not found in the text file.")
                return None

        # Extract fields based on known patterns
        data['Company Name'] = extract_field(r'Company Name:(.+)', content, 'Company Name')
        data['Founded'] = extract_field(r'Founded:(.+)', content, 'Founded')
        data['CEO'] = extract_field(r'CEO:(.+)', content, 'CEO')
        data['Industry'] = extract_field(r'Industry:(.+)', content, 'Industry')
        data['Revenue'] = extract_field(r'Revenue:(.+)', content, 'Revenue')
        data['Net Income'] = extract_field(r'Net Income:(.+)', content, 'Net Income')
        data['Main Products'] = extract_field(r'Main Products:(.+)', content, 'Main Products')
        data['Number of Employees'] = extract_field(r'Number of Employees:(.+)', content, 'Number of Employees')
        data['Headquarters'] = extract_field(r'Headquarters:(.+)', content, 'Headquarters')
        data['Website'] = extract_field(r'Website:(.+)', content, 'Website')
        data['Operating Income'] = extract_field(r'Operating Income:(.+)', content, 'Operating Income')
        data['Market Capitalization'] = extract_field(r'Market Capitalization:(.+)', content, 'Market Capitalization')
        data['Profit Margin'] = extract_field(r'Profit Margin:(.+)', content, 'Profit Margin')
        data['Return on Equity (ROE)'] = extract_field(r'Return on Equity \(ROE\):(.+)', content, 'Return on Equity (ROE)')
        data['Debt to Equity Ratio'] = extract_field(r'Debt to Equity Ratio:(.+)', content, 'Debt to Equity Ratio')
        data['Current Ratio'] = extract_field(r'Current Ratio:(.+)', content, 'Current Ratio')
        data['P/E Ratio'] = extract_field(r'P/E Ratio:(.+)', content, 'P/E Ratio')
        data['Dividend Yield'] = extract_field(r'Dividend Yield:(.+)', content, 'Dividend Yield')
        data['Revenue Growth (YoY)'] = extract_field(r'Revenue Growth \(YoY\):(.+)', content, 'Revenue Growth (YoY)')
        data['R&D Expenses'] = extract_field(r'R&D Expenses:(.+)', content, 'R&D Expenses')
        data['Customer Acquisition Cost'] = extract_field(r'Customer Acquisition Cost:(.+)', content, 'Customer Acquisition Cost')
        data['Customer Lifetime Value'] = extract_field(r'Customer Lifetime Value:(.+)', content, 'Customer Lifetime Value')
        data['Market Share'] = extract_field(r'Market Share:(.+)', content, 'Market Share')
        data['Competitors'] = extract_field(r'Competitors:(.+)', content, 'Competitors')
        data['Recent News'] = extract_field(r'Recent News:(.+)', content, 'Recent News')
        data['Future Outlook'] = extract_field(r'Future Outlook Summary :(.+)', content, 'Future Outlook')
        data['ESG Initiatives'] = extract_field(r'ESG Initiatives:(.+)', content, 'ESG Initiatives')

    except Exception as e:
        print(f"An error occurred while reading the text file: {e}")
    
    return data

def map_fields_to_pdf(extracted_data):
    """Map the extracted data to the corresponding PDF form fields."""
    mapped_data = {}
    rules = {
        'Text-OrN6IEuUMK': 'Company Name',
        'Text-_NjjkC36_y': 'Founded',
        'Text-R5QrMNRgBI': 'CEO',
        'Text-t7jthyYnmR': 'Industry',
        'Text-FjLkuiZK7W': 'Revenue',
        'Text-NyiEFw8Q73': 'Net Income',
        'Text-r8WYKkKnF5': 'Main Products',
        'Text-Ftzrb-tq1p': 'Number of Employees',
        'Text-1eXkNHJD3o': 'Headquarters',
        'Text-kmd8gDGQr5': 'Website',
        'Text-3wFskU85I1': 'Operating Income',
        'Text-1Z98_16rNR': 'Market Capitalization',
        'Text-3PhzHkBoTy': 'Profit Margin',
        'Text-4RmI85phMZ': 'Return on Equity (ROE)',
        'Text-L8cf1b5HSH': 'Debt to Equity Ratio',
        'Text-PyO5Ep61Hu': 'Current Ratio',
        'Text-9eS5I9ALsB': 'P/E Ratio',
        'Text-3gJPsDhe9O': 'Dividend Yield',
        'Text-8U0GZc91Li': 'Revenue Growth (YoY)',
        'Text-NGQezHBuAX': 'R&D Expenses',
        'Text-LndjQt97gS': 'Customer Acquisition Cost',
        'Text-ZIXBcKIn2h': 'Customer Lifetime Value',
        'Text-5b4Zy7Qz3y': 'Market Share',
        'Text-7Cka8b9QGx': 'Competitors',
        'Text-KMcNPu7pFe': 'Recent News',
        'Text-9phO6QJcBt': 'Future Outlook',
        'Text-CcNlPQMa7C': 'ESG Initiatives',
    }
    
    for pdf_field, data_key in rules.items():
        if data_key in extracted_data:
            mapped_data[pdf_field] = extracted_data[data_key]
        else:
            print(f"Field {data_key} not found in extracted data.")
    
    return mapped_data

def fill_pdf_form(input_pdf, output_pdf, data):
    """Fills the PDF form using the mapped data."""
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # Fill form fields with mapped data
    writer.add_page(reader.pages[0])

    # Fill in the form fields
    writer.update_page_form_field_values(writer.pages[0], data)

    # Write the filled form to a new PDF
    with open(output_pdf, "wb") as out_pdf:
        writer.write(out_pdf)

def main():
    # Load the knowledge database from the text file
    extracted_data = load_data_from_text('Dummy_data.txt')

    # Open the PDF form and fill it
    mapped_data = map_fields_to_pdf(extracted_data)
    fill_pdf_form('data/Dummy_Questionnaire.pdf', 'output/filled_form.pdf', mapped_data)

if __name__== "_main_":
    main()