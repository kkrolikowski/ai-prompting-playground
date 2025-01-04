# AI Prompting Playground

The script is used to generate data based on a prompt sent to AI on any topic. 
The project is inspired by the course: [The Complete Prompt Engineering Bootcamp](https://www.udemy.com/share/108qiI3@sgH5wYaMGJsfCjcxvUlJ8rtSP7jw3vqyhz5AquPq_ibvHy5PEbsGGITf5EY5SaL7/)

## Prerequisites

- An active account on [OpenAI](https://platform.openai.com/docs/overview)
- API Key: [https://platform.openai.com/settings/organization/api-keys](https://platform.openai.com/settings/organization/api-keys)
- python3

## Installation

```bash
git clone git@github.com:kkrolikowski/ai-prompting-playground.git
cd ai-prompting-playground
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
mv .env-example .env
```

> ☝️ The generated OpenAI token should be saved in the .env file.

## Usage

In the `templates` directory, there is a sample prompt file: `article_outline.j2`. It is a [Jinja2](https://jinja.palletsprojects.com/en/stable/) template equipped with logic that allows generating data using AI in several formats:

- JSON
- Markdown
- YAML

In the file run.py, the following code handles data generation according to the specified format:

```python
prompt = ai.prompt_render({
  "variables": {"article": "What is data engineering?", "format": "yaml"},
  "template": "article_outline"
})
```

### Variables

- `variables` contains the variables that are passed directly to the Jinja template.
- `template` the value of this option is the file name without the extension, which is located in the `templates` directory.

## Adding prompts

To add a new prompt, you need to create a new file in `templates` with the extension: `.j2`. The file can be freely rendered using Jinja. The file name and variables used to construct the prompt are configured in the `run.py` file according to the above example.
