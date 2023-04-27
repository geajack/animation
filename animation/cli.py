import argparse
import importlib
import animation


def main():
    argument_parser = argparse.ArgumentParser(add_help=False)

    argument_parser.add_argument("render_function", type=str)
    argument_parser.add_argument("--fps", type=int, default=60, nargs="?")
    argument_parser.add_argument("--w", type=int, default=800, nargs="?")
    argument_parser.add_argument("--h", type=int, default=800, nargs="?")
    argument_parser.add_argument("--o", type=str, default=None, nargs="?")
    argument_parser.add_argument("--np", action="store_true", default=False)
    argument_parser.add_argument("--s", action="store_true", default=False)
    argument_parser.add_argument("--help", action="help")

    arguments = argument_parser.parse_args()

    halves = arguments.render_function.rsplit(":")
    module_path = halves[0]
    if len(halves) > 1:
        function_name = halves[1]
    else:
        function_name = "render"
    
    module = importlib.import_module(module_path)
    render_function = getattr(module, function_name)

    animation.animate(
        render_function,
        arguments.fps,
        arguments.w,
        arguments.h,
        filename=arguments.o,
        preview=not arguments.np,
        silent=arguments.s if arguments.s else None,
    )

