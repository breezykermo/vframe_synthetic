# --------------------------------------------------------
# add/edit commands in commands/admin directory
# --------------------------------------------------------

import click

from app.settings import app_cfg
from app.utils import log_utils
from app.commands.factory import ClickSimple

# click cli factory
cc = ClickSimple.create(app_cfg.DIR_COMMANDS_BLENDER)

# --------------------------------------------------------
# CLI
# --------------------------------------------------------
@click.group(cls=cc, chain=False)
@click.option('-v', '--verbose', 'verbosity', count=True, default=4,
  show_default=True,
  help='Verbosity: -v DEBUG, -vv INFO, -vvv WARN, -vvvv ERROR, -vvvvv CRITICAL')
@click.pass_context
def cli(ctx, **kwargs):
  """\033[1m\033[94mVFRAME: Blender Scripts\033[0m
  """
  ctx.opts = {}
  # init logger
  log_utils.Logger.create(verbosity=kwargs['verbosity'])


# --------------------------------------------------------
# Entrypoint
# --------------------------------------------------------
if __name__ == '__main__':
    cli()

