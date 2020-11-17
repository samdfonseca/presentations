def adjust_scheduled_ds(num_days: int):
    """
    Adds `num_days` to the DagRun execution_date if the run was triggered via the scheduler.
    """
    nodash_format = "%Y%m%d"
    dash_format = "%Y-%m-%d"

    def func(ds: str, dag_run: DagRun):
        if dag_run.external_trigger:
            # if dag run is manually triggered, don't adjust ds
            return ds
        nodash = ds.isdigit() and len(ds) == 8
        if nodash:
            # convert ds_nodash to ds for ds_add
            ds = macros.ds_format(ds, nodash_format, dash_format)
        # dag run is scheduler triggered, so add num_days to ds
        ds = macros.ds_add(ds, num_days)
        if nodash:
            # return ds in format it was given
            return macros.ds_format(ds, dash_format, nodash_format)
        return ds

    return func

