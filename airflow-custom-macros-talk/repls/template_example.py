import json
import sys

from jinja2 import Environment, FileSystemLoader, Template


env = Environment(
        loader=FileSystemLoader('./code'),
        lstrip_blocks=True,
        trim_blocks=True,
)

tmpl = env.get_template('template_example.sh')

data = json.load(sys.stdin)

print(tmpl.render(**data))

