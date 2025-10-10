
# GoGroup SEO/GEO

This repository contains SEO and GEO specific resources for [gogroup](https://www.gogroup.co/) and [goteams](https://www.goteams.de/) sites. The content is locale specific and the project resources can also be accessed via this repo's [github pages link](https://nitin-gogroup.github.io/gogroup-GEO/)

## Project Structure

- **html-mds/**  
	Contains Markdown files for web content in multiple languages (`de`, `en`) for GoGroup and GoTeams pages. These pages are recommended by [llmstxt.org](https://llmstxt.org/) and contain content specifically for llms to read.

- **llms-txts/**  
	Contains `.llm.txt` files with LLM-related content for GoGroup, and GoTeams.

- **schemas/**  
	Contains JSON schema files for the GoGroup sites.

- **test-scripts/**  
	Contains Python scripts for testing and interacting with LLMs.
	- `llms-script.py`
	- `openai-llms-script.py`

## Usage

- Use the Markdown files in `html-mds/` for website content in German and English.
- Use the schemas in `schemas/` to validate the structure of your content.
- Use the scripts in `test-scripts/` to run and test LLM interactions.

## Getting Started

1. Clone the repository.
2. Review the content and schemas for your use case.
3. Run the Python scripts in `test-scripts/` to interact with LLMs.