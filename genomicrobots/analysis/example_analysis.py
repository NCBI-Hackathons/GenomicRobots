
from random import choice


def example_analysis(rsids):
    results = []

    for rs in rsids:
        results.append({
            'rs': rs,
            'status': choice(["NO", "YES", "SORRY"])
        })

    return results
