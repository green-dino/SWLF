import pandas as pd

class CSVConverter:
    def __init__(self, input_csv):
        self.input_csv = input_csv
        self.df = None

    def load_csv(self):
        try:
            self.df = pd.read_csv(self.input_csv)
            print(f"Loaded '{self.input_csv}' successfully.")
        except FileNotFoundError:
            print(f"Error: '{self.input_csv}' not found.")
        except Exception as e:
            print(f"An error occurred while loading the CSV file: {e}")

    def convert_to_json(self, output_json):
        if self.df is not None:
            try:
                self.df.to_json(output_json, orient='records')
                print(f"CSV file '{self.input_csv}' has been converted to JSON and saved as '{output_json}'.")
            except Exception as e:
                print(f"An error occurred while converting to JSON: {e}")
        else:
            print("CSV file is not loaded. Please load the CSV file first.")

    def convert_to_excel(self, output_excel):
        if self.df is not None:
            try:
                self.df.to_excel(output_excel, index=False, engine='openpyxl')
                print(f"CSV file '{self.input_csv}' has been converted to Excel and saved as '{output_excel}'.")
            except Exception as e:
                print(f"An error occurred while converting to Excel: {e}")
        else:
            print("CSV file is not loaded. Please load the CSV file first.")

def main():
    input_csv = input("Enter the path to the CSV file: ")
    converter = CSVConverter(input_csv)

    while True:
        output_format = input("Enter the desired output format (json or excel, or 'quit' to exit): ")
        if output_format == "json":
            output_json = input("Enter the path for the output JSON file: ")
            converter.load_csv()
            converter.convert_to_json(output_json)
        elif output_format == "excel":
            output_excel = input("Enter the path for the output Excel file: ")
            converter.load_csv()
            converter.convert_to_excel(output_excel)
        elif output_format == "quit":
            break
        else:
            print("Unsupported output format. Please choose 'json' or 'excel'.")

if __name__ == "__main__":
    main()
