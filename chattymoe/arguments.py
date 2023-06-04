"""
    pararses chattymoe arguments and keyword arguments
    args are provided by a function call to mk_args()
    
    RUN like:
    import chattymoe.arguments
    kwargs.updeate(arguments.mk_args().__dict__)
"""
import argparse


def mk_args():
    parser = argparse.ArgumentParser(description="run: python -m chattymoe info")
    parser.add_argument(
        "action", metavar="action", nargs=None, help="chattymoe.actions/chats or a prompt"
    )
    parser.add_argument(
        "-l",
        "--lang",
        required=False,
        nargs=None,
        const=None,
        type=str,
        default='en',
        help="language to use",
    )

    parser.add_argument(
        "-m",
        "--model",
        required=False,
        nargs=None,
        const=None,
        type=str,
        default="gpt-3.5-turbo",
        help="openAi model to use",
    )

    parser.add_argument(
        "-c",
        "--chat",
        required=False,
        nargs=None,
        const=None,
        type=str,
        default='empty',
        help="chat template you want to use, see settings.chatsDir",
    )

    parser.add_argument(
        "-p",
        "--cwd",
        required=False,
        nargs=None,
        const=None,
        type=str,
        default='C:/temp',
        help="workPath/working directory to use moe in",
    )

    parser.add_argument(
        "-o",
        "--origin",
        required=False,
        nargs=None,
        const=None,
        type=str,
        default='action',
        help="default source / origin of prompt i.e. action, audio, text, system",
    )

    parser.add_argument(
        "-a",
        "--app",
        required=False,
        nargs=None,
        const=None,
        type=str,
        default=None,
        help="app to use chat for i.e. see settings.appsDir",
    )

    parser.add_argument(
        "-t",
        "--test",
        required=False,
        nargs="?",
        const=True,
        type=bool,
        default=False,
        help="test response, for testing you can enter chatgpts expected response",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        required=False,
        nargs="?",
        const=1,
        type=int,
        default=1,
        help="rewpond with - 1:no explanation, 2:short explanation, 3:detailed explanation",
    )

    parser.add_argument(
        "-y",
        "--yes",
        required=False,
        nargs="?",
        const=True,
        type=bool,
        default=False,
        help="send prompt without user confirmation",
    )

    parser.add_argument(
        "-r",
        "--raw",
        required=False,
        nargs="?",
        const=True,
        type=bool,
        default=False,
        help="send prompt as typed without any modifications",
    )

    return parser.parse_args()
