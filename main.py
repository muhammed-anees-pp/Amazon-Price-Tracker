from itertools import product
from locale import currency

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


# RENDER PRODUCT CARD
def render_product_card(product):
    with streamlit.container(border=True):
        columns = streamlit.columns([1,2])

        try:
            images = product.get("images",[])
            if images and len(images) > 0:
                columns[0].image(images[0], width=200)
            else:
                columns[0].write("No image found")
        except:
            columns[0].write("Error loading image")

        with columns[1]:
            streamlit.subheader(product.get("title") or product["product_code"])
            info_columns = streamlit.columns(3)
            currency = product.get("currency", "")
            price = product.get("price","-")
            info_columns[0].metric("Price", f"{currency} {price}" if currency else price)
            info_columns[1].write(f"Brand: {product.get('brand', '-')}")
            info_columns[2].write(f"Product: {product.get('product', '-')}")

            domain_info = f"amazon.{product.get('amazon_domain', 'com')}"
            geo_info = product.get("geo_location", "")
            streamlit.caption(f"Domain: {domain_info} | Geo Location: {geo_info}")

            streamlit.write(product.get("url",""))
            if streamlit.button("Start analyzing competitors", key=f"analyze_{product['product_code']}"):
                streamlit.session_state["analyzing_product_code"] = product["product_code"]


# APPLICATION ENTRY
def main():
    streamlit.set_page_config(page_title="Amazon Price Tracker", page_icon="📊", layout="wide")
    render_title()
    product_code, postal_code, domain = render_input()

    if streamlit.button("Scrape Product") and product_code:
        with streamlit.spinner("Scrapping..."):
            product = scrape_product_details(product_code, postal_code, domain)
        streamlit.success("Product scrapped successfully")
        render_product_card(product)

if __name__ == "__main__":
    main()