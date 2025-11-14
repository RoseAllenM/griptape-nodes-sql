# Imports

import logging
from base_sql_node import BaseSQLNode
from griptape_nodes.exe_types.core_types import Parameter, ParameterMode
from typing import Any, Optional


# Globals

logger = logging.getLogger(__name__)


# Classes


class SelectFromTable(BaseSQLNode):
    """Get the contents of a SQL Table as a list."""

    def __init__(self, name: str, metadata: Optional[dict[str, Any]] = None, **kwargs):
        super().__init__(name=name, metadata=metadata, **kwargs)

        self.add_parameter(
            Parameter(
                name="headers",
                input_types=["str"],
                type="str",
                output_type="str",
                tooltip="A comma-separated list of column headers to return.  If not "
                "supplied, all columns will be returned.",
            )
        )

        self.add_parameter(
            Parameter(
                name="single_value",
                input_types=["bool"],
                type="bool",
                output_type="bool",
                default_value=False,
                tooltip="If true AND a single column is specified, return just a list "
                "of those values.",
            )
        )

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
        single = False

        headers = self.parameter_values.get("headers", "").split(",")
        headers = [header.strip() for header in headers if header]

        if headers and headers != ["*"]:
            select = ", ".join(headers)
            if len(headers) == 1:
                single = self.parameter_values["single_value"]
        else:
            headers = [
                column[1]
                for column in self.execute("PRAGMA table_info({table})").fetchall()
            ]
            select = "*"

        rows = self.execute(f"SELECT {select} FROM {{table}}").fetchall()

        if single:
            self.parameter_output_values["output"] = [row[0] for row in rows]
        else:
            self.parameter_output_values["output"] = [
                dict(zip(headers, row)) for row in rows
            ]

        super().process()
