"""
This file performs portfolio rebalancing, presenting the results
confluent with Vanguard Switch procedures. For example, if you hold
assets "A", "B", and "C" on Vanguard, each with total values in your
portfolio of 2000, 3000, and 4000, respectively. By running:
`rebalance A 2000 B 3000 C 4000`
You will be presented with:
`{'A': 1.0, 'B': 0.0, 'C': -0.25}`,
indicating that you should sell 25% of "C", placing 100% of the sale
into "A" and 0% into "B".
"""

import sys

from portfolio_rebalance import __version__

__author__ = "David Simmons"
__copyright__ = "David Simmons"
__license__ = "MIT"


def rebalance(dict):
    """Portfolio rebalancer

    Args:
      kwargs (Dict): Dictionary of assets and total portfolio value

    Returns:
      Dict: Dictionary of assets and percentage to be sold/bought 
    """
    total = 0.0 
    for key, value in dict.items():
        total += value

    rebalanced_asset_value = total / len(dict)
    rebalanced_assets = {}

    for key, value in dict.items():
        rebalanced_assets[key] = rebalanced_asset_value / dict[key] - 1
    
    value_of_buys = 0
    for key, value in rebalanced_assets.items():
        if value > 0:
            value_of_buys += value
        else:
            pass

    for key, value in rebalanced_assets.items():
        if value > 0:
            print(value)
            rebalanced_assets[key] /= value_of_buys
        else:
            pass

    return rebalanced_assets

def parse_args(args):
    """Parse command line parameters

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--help"]``).

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    keys = []
    values = []
    for asset in args:
        try:
            is_float = float(asset)
        except ValueError:
            is_float = False
        if isinstance(asset, str) and not is_float:
            keys.append(asset)
        elif is_float:
            values.append(float(asset))
        else:
            raise Exception()
    if len(keys) != len(values):
        raise Exception()
    
    assets = {}
    for idx, el in enumerate(keys):
        assets[el] = values[idx]
            
    return assets


def main(args):
    kwargs = parse_args(args)
    print(rebalance(kwargs))


def run():
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
