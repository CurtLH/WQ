import click
from click.testing import CliRunner
from wq import cli


def test_wq_cli():
    runner = CliRunner()
    result = runner.invoke(cli.cli, ['--help'])
    assert result.exit_code == 0
    assert 'API Access to Wunderground' in result.output
