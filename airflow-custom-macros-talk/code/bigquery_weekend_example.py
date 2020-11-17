# Select from `proj.dataset.table1` when execution_date is a weekday,
# from `proj.dataset.table2` when execution_date is a weekend.

BigQueryOperator(
        ...,
        sql="""
            SELECT
                *
            FROM
                {% if execution_date.weekday() < 5 -%}
                    `proj.dataset.table1`
                {% else -%}
                    `proj.dataset.table2`
                {%- endif %}
            """,
)
