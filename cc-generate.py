try:
    from command_center.__main__ import COMMANDS, parse_args, main
except ModuleNotFoundError:
    import pathlib
    import sys

    PROJ_ROOT = pathlib.Path(__file__).parent
    PATH_ENTRY = str(PROJ_ROOT / 'lib')
    sys.path.insert(0, PATH_ENTRY)

    from command_center.__main__ import COMMANDS, parse_args, main


cmd, cmd_kwargs = parse_args(subset='generate')
main(cmd, cmd_kwargs)
