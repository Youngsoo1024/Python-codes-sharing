import re

def extract_prices_from_txt(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
        
    pattern = r"Total\n\$(\d{2}\.\d{2})?"  # \$ for literal dollar sign, (\.\d{2})? for optional decimal part
    
    # finding all matching price and extracting the first element (price string) from the results
    prices = re.findall(pattern, text)
    extracted_prices = [price[:] for price in prices]
    
    return extracted_prices

# 'extracted_text.txt' extract price from txt file
file_name = 'extracted_text.txt' 
extracted_prices = extract_prices_from_txt(file_name)
print("all list extracted: ", extracted_prices)
print("average: " , sum(map(float, extracted_prices))/len(extracted_prices))
print("summation: " , sum(map(float, extracted_prices)))
