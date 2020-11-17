# Return result_true if execution_date is a weekend,
# otherwise return result_false.
def if_weekend(result_true, result_false) -> callable:
    def func(execution_date: pendulum.Pendulum):
        if execution_date.weekday() >= 5:
            return result_true
        return result_false
    return func


with DAG(...,
        user_defined_macros={
            "determine_table": if_weekend('proj.dataset.table2', 'proj.dataset.table1'),
        },
    ) as dag:

    BigQueryOperator(
            ...,
            sql="SELECT * FROM `{{ determine_table(execution_date) }}`",
    )
