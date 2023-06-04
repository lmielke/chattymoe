"""
    Entry poiont for chattymoe shell calls 
    ###################################################################################
    
    __main__.py imports the action module from chattymoe.actions >> actionModule.py
                and runs it
                action is provided as first positional argument

    ###################################################################################
    
    example: 
        python -m chattymoe info
    above cmd is identical to
        python -m chattymoe.actions.info


"""

import colorama as color

color.init()
import importlib

import chattymoe.settings as sts
import chattymoe.arguments as arguments
import chattymoe.contracts as contracts


def runable(*args, action, **kwargs):
    """
    imports action as a package and executes it
    returns the runable result
    """
    return importlib.import_module(f"chattymoe.actions.{action}")


def main(*args, **kwargs):
    """
    to runable from shell these arguments are passed in
    runs action if legidemit and prints outputs
    """
    kwargs = arguments.mk_args().__dict__

    # kwargs are vakidated against enforced contract
    kwargs = contracts.checks(*args, **kwargs)
    if kwargs.get("action") != "help":
        return runable(*args, **kwargs).main(*args, **kwargs)


if __name__ == "__main__":
    main()
