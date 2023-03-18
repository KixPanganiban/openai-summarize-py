from setuptools import setup

setup(
    name="openai_summarize",
    version="0.1.4",
    description="Summarize long text using OpenAI's text-davinci-003 model.",
    author="Kix Panganiban",
    author_email="kixpanganiban@protonmail.com",
    packages=["openai_summarize"],
    install_requires=[
        "aiohttp==3.8.4",
        "aiosignal==1.3.1",
        "async-timeout==4.0.2",
        "attrs==22.2.0",
        "certifi==2022.12.7",
        "charset-normalizer==3.1.0",
        "frozenlist==1.3.3",
        "idna==3.4",
        "multidict==6.0.4",
        "openai==0.27.2",
        "regex==2022.10.31",
        "requests==2.28.2",
        "tiktoken==0.3.2",
        "tqdm==4.65.0",
        "urllib3==1.26.15",
        "yarl==1.8.2",
    ],
)
