import streamlit



# RENDER THE APPLICATION HEADER
def render_title():
    streamlit.title("Amazon Price Tracker")
    streamlit.caption("Enter Your Product Code to Get Product Insights")


# RENDER THE UESR INPUT FORM
def render_input():
    product_code = streamlit.text_input("Product Code", placeholder="e.g., BCD2341BE")
    postal_code = streamlit.text_input("Zip/Postal Code/Pin Code", placeholder="e.g., 676489")
    domain = streamlit.selectbox("Domain", [
        "com", "ca", "de", "fr", "it", "ae", "co.uk"
    ])
    return product_code.strip(), postal_code.strip(), domain


# APPLICATION ENTRY
def main():
    streamlit.set_page_config(page_title="Amazon Price Tracker", page_icon="📊")
    render_title()
    product_code, postal_code, domain = render_input()

if __name__ == "__main__":
    main()