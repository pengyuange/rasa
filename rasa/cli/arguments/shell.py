from rasa.cli.arguments.default_arguments import add_model_param, add_logging_options
from rasa.cli.arguments.run import add_run_arguments


def add_shell_arguments(parser):
    add_run_arguments(parser)
    add_model_param(parser)

    add_logging_options(parser)


def add_shell_nlu_arguments(parser):
    add_model_param(parser)

    add_logging_options(parser)
