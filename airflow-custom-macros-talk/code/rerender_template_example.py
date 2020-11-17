def rerender(subtemplate: str, task_instance: TaskInstance) -> str:
    """
    Ex.
        ```
        BigQueryCreateExternalTableOperator(
            destination_project_dataset_table="project.dataset.{{rerender(params.table_id, ti)}}",
            params={"table_id": "some_table_{{ds_nodash}}"},
            ...
        )
        # Is the same as:
        BigQueryCreateExternalTableOperator(
            destination_project_dataset_table="project.dataset.some_table_{{ds_nodash}}",
            ...
        )
        ```
    """
    jinja_context = task_instance.get_template_context()
    jinja_env = jinja2.Environment(cache_size=0)
    if hasattr(task_instance, "task") and hasattr(task_instance.task, "dag"):
        if task_instance.task.dag.user_defined_macros:
            jinja_context.update(dag.user_defined_macros)
        jinja_env = task_instance.task.dag.get_template_env()
    return jinja_env.from_string(subtemplate).render(**jinja_context)

