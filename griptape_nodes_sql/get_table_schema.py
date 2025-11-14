# Imports

import logging
from base_sql_node import BaseSQLNode
from griptape_nodes.exe_types.core_types import Parameter, ParameterMode
from typing import Any, Optional


# Globals

logger = logging.getLogger(__name__)


# Classes


class GetTableSchema(BaseSQLNode):
    """Get the schema for the SQL Table."""

    def __init__(self, name: str, metadata: Optional[dict[str, Any]] = None, **kwargs):
        super().__init__(name=name, metadata=metadata, **kwargs)

        self.add_parameter(
            Parameter(
                name="output",
                type="str",
                tooltip="The SQL statement defining the Table.",
                allowed_modes={ParameterMode.OUTPUT},
            )
        )

    def process(self):
        """Set Node's parameter_output_values and close the SQL connection."""
        self.parameter_output_values["output"] = self.execute(
            "SELECT sql FROM sqlite_master WHERE tbl_name = '{table}'"
        ).fetchone()[0]

        super().process()
