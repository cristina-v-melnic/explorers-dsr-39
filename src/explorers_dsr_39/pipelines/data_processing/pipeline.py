from kedro.pipeline import Pipeline, node, pipeline

from .nodes import impute_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=impute_data,
                inputs="train_data",
                outputs="train_data_dropna",
                name="example_pipeline",
            )
        ]
    )
