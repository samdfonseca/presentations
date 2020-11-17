#!/usr/bin/env bash

{% if names -%}
  {% for name in names -%}
    echo "Hello {{ capitalize(name) }}!"
  {% endfor %}
{% else -%}
  echo "Hello World!"
{%- endif %}
