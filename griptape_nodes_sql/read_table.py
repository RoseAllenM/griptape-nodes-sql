# Imports

import logging
from base_sql_node import BaseSQLNode
from griptape_nodes.exe_types.core_types import Parameter, ParameterMode
from typing import Any, Optional


# Globals

logger = logging.getLogger(__name__)


# Classes


class ReadTable(BaseSQLNode):
    """Get the full contents of a SQL Table as a list of dictionaries."""

    def __init__(self, name: str, metadata: Optional[dict[str, Any]] = None, **kwargs):
        super().__init__(name=name, metadata=metadata, **kwargs)

        self.add_parameter(
            Parameter(
                name="output",
                type="json",
                tooltip="The extracted value(s)",
                allowed_modes={ParameterMode.OUTPUT},
            )
        )

    def process(self):
        """Set Node's parameter_output_values and close the SQL connection."""
        headers = [column[1] for column in self.execute("PRAGMA table_info({table})")]

        self.parameter_output_values["output"] = [
            dict(zip(headers, row)) for row in self.execute("SELECT * FROM {table}")
        ]

        super().process()
