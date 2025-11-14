# Imports

import json
import logging
from base_sql_node import BaseSQLNode
from griptape_nodes.exe_types.core_types import Parameter, ParameterMode
from typing import Any, Optional


# Globals

logger = logging.getLogger(__name__)


# Classes


class InsertRows(BaseSQLNode):
    """Write rows of data into the SQL Table."""

    def __init__(self, name: str, metadata: Optional[dict[str, Any]] = None, **kwargs):
        super().__init__(name=name, metadata=metadata, **kwargs)

        self.add_parameter(
            Parameter(
                name="data",
                input_types=["json"],
                type="json",
                tooltip="The data to insert into the table.  This should be a single "
                "dictionary or a list of dictionaries each with the same keys.",
                allowed_modes={ParameterMode.INPUT},
            )
        )

    def process(self):
        """Set Node's parameter_output_values and close the SQL connection."""
        data = self.parameter_values["data"]

        if isinstance(data, str):
            data = json.loads(data)

        if isinstance(data, dict):
            data = [data]

        headers = [f":{key}" for key in data[0].keys()]

        self.executemany(f"INSERT INTO {{table}} VALUES ({', '.join(headers)})", data)

        super().process()
