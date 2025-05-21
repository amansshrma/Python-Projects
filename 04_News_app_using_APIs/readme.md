
# News App using NewsAPI

This is a command-line Python project that fetches the latest top headlines from the US using the [NewsAPI](https://newsapi.org/). The user can choose a category of interest, and the app will display related news headlines.

## Features

- Fetches real-time news from the US.
- User can select from various news categories.
- Uses `dotenv` to manage API keys securely.
- Includes input validation and error handling.

## Prerequisites

- Python 3.x
- A NewsAPI key (get it for free at [https://newsapi.org/register](https://newsapi.org/register))

## Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/amansshrma/Python-Projects.git
cd Python-Projects/04_News_app_using_APIs
```

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Create a `.env` file and add your API key:**

```
NEWS_API_KEY=your_api_key_here
```

## How to Run

```bash
python news_app.py
```

Follow the on-screen instructions to choose a news category and read top headlines.

## Dependencies

- requests
- python-dotenv

You can install them using:

```bash
pip install requests python-dotenv
```

## Example

```
What type of US news are you interested in today?
1. business
2. entertainment
3. general
4. health
5. science
6. sports
7. technology
Choose from (1-7)
>>
```

## License

This project is licensed under the MIT License.

---

GitHub: [@amansshrma](https://github.com/amansshrma)
