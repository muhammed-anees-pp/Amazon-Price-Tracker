# Amazon Price Tracker

A Streamlit application for scraping Amazon product details, storing product snapshots locally, finding competing products, and generating competitor analysis with an LLM.

The app accepts an Amazon ASIN, marketplace domain, and postal or ZIP code, then uses the Oxylabs Amazon scraping API to collect product data. Scraped products are saved in a local TinyDB database and can be used as the starting point for competitor discovery and AI-assisted market analysis.

## Features

- Scrape Amazon product details by ASIN
- Support multiple Amazon marketplaces, including `.com`, `.ca`, `.co.uk`, `.de`, `.fr`, `.it`, `.ae`, and `.in`
- Store product data locally with TinyDB
- Display product images, pricing, brand, marketplace, and location context
- Search for competing products using category and product-title signals
- Fetch detailed competitor information in batches
- Generate concise competitor insights using Google Gemini through LangChain

## Tech Stack

- Python
- Streamlit
- TinyDB
- Oxylabs Amazon Scraper API
- LangChain
- Google Gemini
- uv for dependency management

## Project Structure

```text
.
├── main.py                 # Streamlit application entry point
├── pyproject.toml          # Project metadata and dependencies
├── uv.lock                 # Locked dependency versions
└── src
    ├── db.py               # TinyDB database wrapper
    ├── llm.py              # LLM-based competitor analysis
    ├── oxylabs_client.py   # Oxylabs API integration and normalization
    └── services.py         # Product and competitor workflows
```

## Requirements

- Python 3.14 or later
- uv
- Oxylabs account with Amazon scraping API access
- Google API key with access to the configured Gemini model

## Environment Variables

Create a `.env` file in the project root:

```env
OXYLABS_USERNAME=your_oxylabs_username
OXYLABS_PASSWORD=your_oxylabs_password
OXYLABS_BASE_URL=your_oxylabs_realtime_endpoint
GOOGLE_API_KEY=your_google_api_key
GEMINI_MODEL=gemini_model_name
```

Example `GEMINI_MODEL` value:

```env
GEMINI_MODEL=gemini-2.5-flash
```

## Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/your-username/amazon-price-tracker.git
cd amazon-price-tracker
uv sync
```

If you are not using `uv`, install the dependencies from `pyproject.toml` with your preferred Python package manager.

## Running the App

Start the Streamlit application:

```bash
uv run streamlit run main.py
```

Then open the local Streamlit URL shown in the terminal.

## Usage

1. Enter an Amazon ASIN.
2. Enter a ZIP or postal code for location-aware results.
3. Select the Amazon marketplace domain.
4. Click **Scrape Product** to fetch and save product details.
5. Click **Start analyzing competitors** on a saved product.
6. Refresh competitors if needed.
7. Click **Analyze with LLM** to generate a market and competitor summary.

## Data Storage

Product and competitor records are stored locally in `data.json` using TinyDB. This file is created automatically when the application saves its first product.

## Notes

- The quality of competitor discovery depends on the product title, category data returned by Oxylabs, and marketplace availability.
- API usage may incur costs depending on your Oxylabs and Google AI pricing plans.
- Keep `.env` and `data.json` out of version control if they contain private credentials or scraped business data.

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
