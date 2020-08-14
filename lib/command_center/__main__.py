import sys

##################################
# the commands

def cmd_generate():
    raise NotImplementedError


COMMANDS = {
    'generate': cmd_generate,
}


##################################
# the script

def parse_args(argv=sys.argv[1:], prog=sys.argv[0], subset=None):
    import argparse
    parser = argparse.ArgumentParser(
        prog=prog,
    )

    if isinstance(subset, str):
        parser.set_defaults(cmd=subset)
        # XXX Directly add that command's args to the parser.
    else:
        if subset is None:
            cmdnames = subset = list(COMMANDS)
        elif not subset:
            raise ValueError('empty subset')
        elif isinstance(subset, set):
            cmdnames = [k for k in COMMANDS if k in subset]
            subset = sorted(subset)
        else:
            cmdnames = [n for n in subset if n in COMMANDS]
        if len(cmdnames) < len(subset):
            bad = tuple(n for n in subset if n not in COMMANDS)
            raise ValueError(f'unsupported subset {bad}')
        subs = parser.add_subparsers(dest='cmd')
        for cmdname in cmdnames:
            sub = subs.add_parser(cmdname)
            # XXX Add the command's args.
            ...

    args = parser.parse_args(argv)
    ns = vars(args)

    cmd = ns.pop('cmd')

    return cmd, ns


def main(cmd, cmd_kwargs):
    try:
        run_cmd = COMMANDS[cmd]
    except KeyError:
        raise ValueError(f'unsupported cmd {cmd!r}')
    run_cmd(**cmd_kwargs)


if __name__ == '__main__':
    cmd, cmd_kwargs = parse_args()
    main(cmd, cmd_kwargs)
