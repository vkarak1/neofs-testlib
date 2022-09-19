from cli.cli_command import NeofsCliCommand
from shell import CommandResult


class NeofsAdmVersion(NeofsCliCommand):
    def get(self) -> CommandResult:
        """Application version

        Returns:
            str: Command string

        """
        return self._execute("", version=True)
