import logging
from typing import Any, Dict

from kedro.framework.hooks import hook_impl
from pandera.errors import SchemaError
from catfood.data_validation.schemas import no_nan_numeric_schema


logger = logging.getLogger(__name__)


class DataValidationHooks:
    SCHEMA_MAPPING = {"model_input_table": no_nan_numeric_schema}

    @hook_impl
    def after_node_run(self, outputs: Dict[str, Any]) -> None:
        self._run_validation(data=outputs)

    def _run_validation(self, data: Dict[str, Any]) -> None:
        for data_set_name, dataset in data.items():
            if data_set_name not in self.SCHEMA_MAPPING:
                continue
            try:
                schema = self.SCHEMA_MAPPING[data_set_name]
                schema(dataset)
                logger.info(
                    f"{data_set_name} passed data validation with schema {schema}."
                )
            except SchemaError:
                logger.error(
                    f"{data_set_name} didn't pass data validation with schema {schema}."
                )
