# Imports

import logging
import sqlite3
from griptape_nodes.exe_types.core_types import Parameter
from griptape_nodes.exe_types.node_types import ControlNode
from typing import Any, Optional

# Globals

logger = logging.getLogger(__name__)


# Classes


class BaseSQLNode(ControlNode):
    """The base-class of all Nodes that interact with a SQLite datbase."""

    def __init__(self, name: str, metadata: Optional[dict[str, Any]] = None, **kwargs):
        super().__init__(name=name, metadata=metadata, **kwargs)

        self._connection = None
        self._cursor = None

        self.add_parameter(
            Parameter(
                name="database_path",
                input_types=["str"],
                type="str",
                output_type="str",
                tooltip="The path to the SQLite database to connect to.",
            )
        )
        self.add_parameter(
            Parameter(
                name="table",
                input_types=["str"],
                type="str",
                output_type="str",
                tooltip="The name of the SQL table to interact with.",
            )
        )

    @property
    def connection(self) -> sqlite3.Connection:
        """Open channel managing transactions to the SQLite database."""
        if self._connection is None:
            self._connection = sqlite3.connect(self.parameter_values["database_path"])
        return self._connection

    @property
    def cursor(self) -> sqlite3.Cursor:
        """The database cursor which is used to execute SQL statements."""
        if self._cursor is None:
            self._cursor = self.connection.cursor()
        return self._cursor

    def execute(self, statement: str) -> sqlite3.Cursor:
        """Execute the given SQL statement."""
        statement = statement.format(**self.parameter_values)
        logger.info("Executing: %s", statement)

        return self.cursor.execute(statement)

    def process(self):
        """Set Node's parameter_output_values and close the SQL connection."""
        if self.connection:
            self.connection.close()

        self._connection = None
        self._cursor = None
