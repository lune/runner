import click
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Context(object):
    """To pass configs from main to subcommands """
    def __init__(self):
        self.debug = False


pass_ctx = click.make_pass_decorator(Context, ensure=True)


@click.group()
@click.option("--debug", default=False, is_flag=True,
              help="Run in debug mode.")
@click.option("--addr", default="/var/tmp/runner/runner.sock", type=str,
              help="Address to listen on for gRPC API.")
@click.pass_context
def main(ctx, debug, addr):
    ctx.debug = debug
    ctx.addr = addr
    if debug:
        logger.setLevel(logging.DEBUG)


"""
Commands:
- start
- delete
- list
- logs
- server
- status
"""


@main.group()
@click.pass_context
def start(ctx):
    """Starts a job
    """


@start.command("run")
@click.option("--name", help="Job name")
@click.option("--artifacts", required=False, help="Location of the artifacts")
@click.option("--cmd", help="Command to run", required=True)
@click.option("--email", help="Mail address to notify")
@pass_ctx
def run(ctx, name, artifacts, cmd, email):
    """
    This is a doc string
    """
    logger.info("g")
    click.echo("Hello, %s" % (name))
