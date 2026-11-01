from pathlib import Path

import yaml
from jinja2 import Template

# apps/api/src — relative prompt paths like "api/agents/prompts/x.yaml" resolve against this,
# so the code works regardless of the current working directory.
SRC_ROOT = Path(__file__).resolve().parents[3]


def prompt_template_config(yaml_file, prompt_key):
    path = Path(yaml_file)
    if not path.is_absolute():
        path = SRC_ROOT / path

    with open(path, "r") as file:
        config = yaml.safe_load(file)

    template_content = config["prompts"][prompt_key]

    return Template(template_content)
