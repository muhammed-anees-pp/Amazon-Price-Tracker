from itertools import product

import streamlit
from src.oxylabs_client import scrape_product_details



# RENDER THE APPLICATION HEADER
def render_title():
    streamlit.title("Amazon Price Tracker")
    streamlit.caption("Enter Your Product Code to Get Product Insights")


# RENDER THE UESR INPUT FORM
def render_input():
    product_code = streamlit.text_input("Product Code", placeholder="e.g., BCD2341BE")
    postal_code = streamlit.text_input("Zip/Postal Code/Pin Code", placeholder="e.g., 676489")
    domain = streamlit.selectbox("Domain", [
        "com", "ca", "de", "fr", "it", "ae", "co.uk", "in"
    ])
    return product_code.strip(), postal_code.strip(), domain


# APPLICATION ENTRY
def main():
    streamlit.set_page_config(page_title="Amazon Price Tracker", page_icon="📊")
    render_title()
    product_code, postal_code, domain = render_input()

    if streamlit.button("Scrape Product") and product_code:
        with streamlit.spinner("Scrapping..."):
            product = scrape_product_details(product_code, postal_code, domain)
        streamlit.success("Product scrapped successfully")

if __name__ == "__main__":
    main()