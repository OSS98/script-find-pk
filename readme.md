# Data Analysis & Primary Key Discovery Tool

A Python-based data analysis project for discovering primary keys and analyzing financial data from Excel/CSV files and XML datasets. This project is specifically designed to work with budget entries, general ledger data, and other financial datasets.

## Project Overview

This project provides tools to:
- **Find unique column combinations** that can serve as primary keys in datasets
- **Analyze financial data** from various sources (Excel, CSV, XML, SQLite)
- **Process and deduplicate** large datasets
- **Explore data relationships** between budget and general ledger entries

## Features

### Core Functionality
- **Primary Key Discovery**: Automatically find unique combinations of columns that could serve as primary keys
- **Data Deduplication**: Remove duplicate records from datasets
- **Multi-format Support**: Handle Excel (.xlsx), CSV, XML, and SQLite database files
- **Interactive Analysis**: Jupyter notebooks for exploratory data analysis

### Data Sources Supported
- Budget account entries
- General journal/ledger data
- Revenue and invoice data
- Patient and episode data
- Financial transactions

## Project Structure

```
├── main.py                 # Main script for data processing and deduplication
├── tool.py                 # Core functions for finding unique combinations
├── dataframe.py           # XML data processing utilities
├── requirements.txt       # Python dependencies
├── *.ipynb               # Jupyter notebooks for analysis:
│   ├── Budget.ipynb      # Budget data analysis
│   ├── Actual.ipynb      # Actual financial data analysis
│   ├── onward.ipynb      # Main data exploration
│   ├── gl_head.ipynb     # General ledger headers
│   ├── gl_line.ipynb     # General ledger line items
│   └── DataPreview.ipynb # Data preview and exploration
└── source/               # Data files directory
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd script-find-pk
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Quick Start

1. **Find Primary Keys**:
   ```python
   from tool import find_unique_combinations
   import pandas as pd
   
   # Load your dataset
   df = pd.read_excel('your_data.xlsx')
   
   # Find unique column combinations
   columns_to_check = df.columns.tolist()
   find_unique_combinations(df, columns_to_check)
   ```

2. **Deduplicate Data**:
   ```python
   python main.py
   ```

### Advanced Usage

**Using Jupyter Notebooks**:
- `Budget.ipynb`: Analyze budget data and find primary keys
- `onward.ipynb`: Comprehensive data exploration
- `DataPreview.ipynb`: Quick data overview and profiling

**Key Functions**:

```python
# Find unique combinations (from tool.py)
def find_unique_combinations(df, cols):
    """
    Find all unique combinations of columns that could serve as primary keys
    
    Args:
        df: pandas DataFrame
        cols: list of column names to check
    """
```

## Key Findings

Based on the analysis notebooks, the project has identified several potential primary key combinations:

### Budget Data
- `('JOURNAL_ID', 'JOURNAL_LINE', 'UNPOST_SEQ', 'ACCOUNT')` - Unique combination found

### General Ledger Data
- Journal entries typically require combinations of multiple fields for uniqueness
- Common patterns include combinations of journal_id, line numbers, and account codes

## Data Sources

The project works with various financial data sources:
- **Budget Files**: Excel files containing budget entries
- **General Ledger**: Journal entries and transactions
- **Revenue Data**: Invoice and receipt information
- **Patient Data**: Healthcare-specific transaction data
- **Database**: SQLite database (`vtnlake_onedrive_new.db`)

> **Note**: `vtnlake_onedrive_new.db` database file is stored in Google Drive folder `environment_folder`.

## Requirements

- Python 3.8+
- pandas
- openpyxl (for Excel files)
- jupyter (for notebooks)
- sqlite3 (for database operations)
- awswrangler (for AWS integration)
- boto3 (for AWS services)

See `requirements.txt` for complete dependency list.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Data Privacy

This project handles financial and potentially sensitive data. Ensure proper data handling practices:
- Keep data files secure and encrypted
- Follow your organization's data governance policies
- Don't commit sensitive data to version control

## License

[Add your license information here]

## Contact

[Add contact information here]