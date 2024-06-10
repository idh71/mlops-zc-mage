import mlflow

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
# def export_data(data, *args, **kwargs):
def export_data(dv):
    """
    Exports data to some source.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Output (optional):
        Optionally return any object and it'll be logged and
        displayed when inspecting the block run.
    """
    # Specify your data exporting logic here
    # dv = args[0]
    # lr = args[1]
    
    mlflow.set_tracking_uri("http://127.0.0.1:5001")

    
    mlflow.log_artifact(dv)
    # mlflow.log_model(lr)


