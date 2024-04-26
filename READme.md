# Nigerian Job Site Scraper

This README provides instructions for setting up and running a web scraping application for the Nigerian job site [Nigeria Job](https://www.nigeriajob.com) to collect job listings under the "IT, new technologies" category. The scraped data is then stored in a PostgreSQL database and queried using a Flask application. Additionally, unit tests are provided using pytest.

## Step 1: Run the Scraper

### 1.1 Installation

First, ensure you have Python installed on your system.

Install the necessary Python dependencies by running:

```bash
pip install -r requirements.txt
```

### 1.2 Running the Scraper

Run the `db_model.py` script. This script executes the web scraping job and exports the data into a PostgreSQL database. Ensure you have PostgreSQL installed and running, and configure the database connection parameters within `db_model.py` if necessary.

```bash
python db_model.py
```

This script will scrape job listings from the specified category on the Nigerian job site and store them in the PostgreSQL database.

## Step 2: Run the Flask Application

### 2.1 Installation

Ensure Flask is installed. If not, you can install it using pip:

```bash
pip install Flask
```

### 2.2 Running the Flask App

Run the Flask app by executing `app.py`:

```bash
python app.py
```

The Flask app will start running on your local machine. It provides an API to query the PostgreSQL database for job listings.

## Step 3: Run Unit Tests

### 3.1 Installation

Ensure pytest is installed:

```bash
pip install pytest
```

### 3.2 Running Unit Tests

Run the unit tests using pytest:

```bash
pytest
```

This will execute the unit tests defined in the `test_scraper.py` file to ensure the functionality of the web scraper.

## Additional Notes

- The scraped data may contain nested features in the "technology" and "location" columns. You may need to unnest these columns for easier querying and analysis. Consider implementing this transformation in the `db_model.py` script or within the Flask application.
- Ensure that your system meets all dependencies and requirements mentioned above before running the application and tests.

Feel free to reach out if you encounter any issues or have further questions!

