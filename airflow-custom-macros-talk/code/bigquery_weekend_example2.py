# Select from `proj.dataset.table1` when execution_date is a weekday,
# from `proj.dataset.table2` when execution_date is a weekend.
def determine_table(execution_date: pendulum.Pendulum) -> str:
    if execution_date.weekday() >= 5:
        return 'proj.dataset.table2'
    return 'proj.dataset.table1'


with DAG(...,
        user_defined_macros={
            "determine_table": determine_table,
        },
    ) as dag:

    BigQueryOperator(
            ...,
            sql="SELECT * FROM `{{ determine_table(execution_date) }}`",
    )
