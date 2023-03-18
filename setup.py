from setuptools import setup

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(
    name='openai_summarize',
    version='0.1',
    description='Summarize long text using OpenAI\'s text-davinci-003 model.',
    author='Kix Panganiban',
    author_email='kixpanganiban@protonmail.com',
    packages=['openai_summarize'],
    install_requires=requirements,
)
