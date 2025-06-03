# PakWheels Car Scraper

This project contains a Python script designed to scrape used car listing data from PakWheels.com. It utilizes Selenium for dynamic web page interaction and BeautifulSoup for HTML parsing, saving the extracted information into CSV files.

## Features

*   Navigates through multiple pages of car listings.
*   Extracts key details for each car, including:
    *   Name
    *   Price (converted from 'lacs'/'crore' to a numerical value)
    *   City
    *   Production Year
    *   Kilometers Driven
    *   Engine Type
    *   Engine Capacity (Horsepower field is used for CC)
    *   Transmission Type
    *   Direct Link to the listing
*   Saves scraped data into a CSV file named after the search query (e.g., `Used_Cars_in_Karachi.csv`).
*   Handles different types of listing elements found on PakWheels.
*   Provides progress updates in the console.

## Technology Stack

*   Python 3.x
*   [Selenium](https://www.selenium.dev/): For browser automation and fetching dynamic content.
*   [BeautifulSoup4 (bs4)](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): For parsing HTML content.
*   [lxml](https://lxml.de/): As the HTML parser for BeautifulSoup (recommended for speed).
*   `csv`: Python's built-in module for CSV file operations.

## Prerequisites

Before running the scraper, ensure you have the following installed:

1.  **Python 3.x:** Download from [python.org](https://www.python.org/downloads/).
2.  **Required Python Packages:**
    ```bash
    pip install beautifulsoup4 selenium lxml
    ```
3.  **Microsoft Edge WebDriver:** The script is currently configured to use Microsoft Edge (`webdriver.Edge()`). You need to have `msedgedriver.exe` installed and accessible in your system's PATH, or you can specify its location when instantiating the driver. Download the correct version for your Edge browser from the [Microsoft Edge WebDriver page](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).
    *   Alternatively, you can modify the script to use other browsers like Chrome or Firefox by changing `webdriver.Edge()` to `webdriver.Chrome()` or `webdriver.Firefox()` and ensuring you have the respective WebDriver (ChromeDriver or GeckoDriver).

## Setup and Usage

1.  **Clone the repository (or download the files):**
    ```bash
    git clone https://github.com/al-Jurjani/PakWheels-Web-Scraper
    cd PakWheels-Web-Scraper
    ```
2.  **Create a `files/` directory:** The script saves CSV files into a subdirectory named `files`. Create this directory in the same location as `scraper.py` if it doesn't exist:
    ```bash
    mkdir files
    ```
3.  **Configure the Starting URL (Optional):**
    Open `scraper.py`. The main part of the script that initiates the scraping is:
    ```python
    if __name__ == '__main__':
        total_cars = scrapePages('https://www.pakwheels.com/used-cars/search/-/mk_toyota/tr_automatic/cert_pakwheels-certified/')
        print(f'The total number of cars for your search criteria right now are: {total_cars - 1}')
    ```
    You can change the URL passed to `scrapePages()` to target different search criteria on PakWheels.com.

4.  **Run the Scraper:**
    Execute the Python script from your terminal:
    ```bash
    python scraper.py
    ```
    The script will open Edge browser windows, navigate through pages, and print progress.

## Output

*   The script will create a CSV file inside the `files/` directory.
*   The filename will be derived from the search heading on the PakWheels page (e.g., `Used_Cars_for_Sale_in_Karachi_-_PakWheels_Certified.csv`).
*   The CSV file will contain columns: `name`, `price`, `city`, `production_year`, `km_driven`, `engine_type`, `horsepower` (actually engine cc), `transmission`, `link`.
*   The script also prints the total number of cars found (excluding the header row).

## Files

*   `scraper.py`: The main Python script for web scraping.
*   `scaper.ipynb`: A Jupyter Notebook version containing the same scraping logic, useful for interactive development and testing.

## Important Considerations

*   **Website Structure Changes:** Web scrapers are highly dependent on the HTML structure of the target website. If PakWheels.com changes its layout, this scraper might break and require updates to the selectors.
*   **Ethical Scraping:**
    *   Be respectful of the website's resources. The script includes a `time.sleep(10)` which helps in not overwhelming the server.
    *   Always check PakWheels.com's `robots.txt` and Terms of Service to ensure you are complying with their policies.
*   **Error Handling:** The current script has basic error handling. For more robust scraping, consider adding more comprehensive error checks and retry mechanisms.
*   **Rate Limiting/IP Bans:** Excessive requests can lead to your IP being temporarily or permanently banned. Run the scraper responsibly.

## Future Improvements (Suggestions)

*   Implement more robust error handling (e.g., for missing elements, network issues).
*   Add command-line arguments for the starting URL and output file/directory.
*   Integrate a mechanism to respect `robots.txt`.
*   Add options for different web drivers (Chrome, Firefox) easily.
*   Store data in a database instead of/in addition to CSV.
*   Implement logging for better tracking of the scraping process.

## Disclaimer

This script is provided for educational and informational purposes only. The user is solely responsible for any use of this script and must ensure compliance with all applicable laws and website terms of service. The developers of this script are not responsible for any misuse or violations.
