import openai
from jinja2 import Environment, FileSystemLoader


class AIModel:
    def __init__(self, api_key):
        self.model = "gpt-4o"
        self.tpl_dir = "templates"
        self.api_key = api_key

    def complete(self, prompt):
        try:
            res = openai.chat.completions.create(
                model=self.model, messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return res.choices[0].message.content
        except Exception as err:
            print(f"Error on querying OpenAI: {err}")

    def prompt_render(self, prompt_meta):
        try:
            env = Environment(loader=FileSystemLoader(self.tpl_dir))
            template = env.get_template(f"{prompt_meta['template']}.j2")

            return template.render(**prompt_meta["variables"])
        except Exception as err:
            print(f"Template error occured: {err}")
