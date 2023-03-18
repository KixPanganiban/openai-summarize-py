# OpenAI Summarize

OpenAI Summarize is a Python package that generates summaries of text using OpenAI's text-davinci-003 model. It chunks the input text into smaller pieces and generates summaries for each chunk separately using the OpenAI API. The generated summaries are then combined into a final summary. If the final summary is too long, it is recursively summarized until it reaches the desired length.

## Installation

OpenAI Summarize can be installed from PyPI using pip. Simply run:

```
pip install openai_summarize
```

Alternatively, you can install OpenAI Summarize from Git by cloning the repository and running setup.py:

```
git clone https://github.com/kixpanganiban/openai_summarize.git
cd openai-summarize
python setup.py install
```

## Usage

```python
import openai_summarize

openai_summarizer = openai_summarize.OpenAISummarize("your_openai_token")

text = "This is a long piece of text that needs to be summarized."
summary = openai_summarizer.summarize_text(text)

print(summary)
```

## Examples

Here's an example of how to use OpenAI Summarize to summarize a long piece of text:

```python
import openai_summarize

openai_summarizer = openai_summarize.OpenAISummarize("your_openai_token")

text = """The COVID-19 pandemic, also known as the coronavirus pandemic, is an ongoing pandemic of coronavirus disease 2019 (COVID-19), caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). The virus was first identified in December 2019 in Wuhan, China. The World Health Organization declared a Public Health Emergency of International Concern regarding COVID-19 on 30 January 2020, and later declared a pandemic on 11 March 2020. As of 18 March 2023, more than 472 million cases have been confirmed, with more than 6.5 million deaths attributed to COVID-19, making it one of the deadliest pandemics in history.

Efforts to prevent the spread of COVID-19 include vaccination programs, lockdowns, travel restrictions, and the use of masks and other protective equipment. Vaccines have been developed and authorized for emergency use, with the Pfizer-BioNTech vaccine being the first to receive emergency use authorization in December 2020.

The pandemic has had significant social, economic, and political impacts. Many businesses have closed, and unemployment rates have risen in many countries. The pandemic has also highlighted disparities in access to healthcare and education, and has led to an increase in domestic violence and mental health issues."""

summary = openai_summarizer.summarize_text(text)
print(summary)
```

This generates the following summary:

```
The COVID-19 pandemic is caused by the SARS-CoV-2 virus and has resulted in over 6.5 million deaths worldwide. Efforts to prevent its spread include vaccination programs, lockdowns, travel restrictions, and the use of masks and protective equipment. The pandemic has had significant social, economic, and political impacts, including business closures and rising unemployment rates.
```

Here's another example of how to use OpenAI Summarize to summarize a news article:

```python
from newspaper3k import Article
import openai_summarize

openai_summarizer = openai_summarize.OpenAISummarize("your_openai_token")

article = Article("https://www.nytimes.com/2023/03/18/world/europe/russia-nato-ukraine.html")
article.download()
article.parse()
summary = openai_summarizer.summarize_text(article.text)
print(summary)
```

## API Reference

### `OpenAISummarize` class

#### `__init__(self, openai_token)`

Creates an instance of the `OpenAISummarize` class.

##### Arguments

- `openai_token` (str): Your OpenAI API token.

#### `count_tokens(self, text)`

Counts the number of tokens in a given text.

##### Arguments

- `text` (str): The text to count the tokens of.

##### Returns

- `int`: The number of tokens in the text.

#### `chunk_text(self, text, max_tokens=500)`

Breaks up a given text into chunks of at most `max_tokens` tokens.

##### Arguments

- `text` (str): The text to chunk.
- `max_tokens` (int): The maximum number of tokens allowed in each chunk. Defaults to `500`.

##### Returns

- `list` of `str`: The chunks of text.

#### `summarize_text(self, text, max_chunk_size=500, max_combined_summary_size=4000)`

Generates a summary of a given text using OpenAI's text-davinci-003 model.

##### Arguments

- `text` (str): The text to summarize.
- `max_chunk_size` (int, optional): The size of each chunk of text to summarize. Defaults to `500`.
- `max_combined_summary_size` (int, optional): The maximum size of the combined summary. Defaults to `4000`.

##### Returns

- `str`: The generated summary of the text.

#### `extract_article_text(self, url)`

Extracts the main text content of an article from a given URL.

##### Arguments

- `url` (str): The URL of the article to extract the text from.

##### Returns

- `str`: The main text content of the article.
