# -*- coding: utf-8 -*-

"""A one-time script to get the old NIFT and make a more reasonable format for curation."""

from typing import Set

import pandas as pd
from bel_resources import get_bel_resource

NIFT_URL = 'https://raw.githubusercontent.com/neurommsig/neurommsig-terminology/master/terminologies/neuroimaging-feature-terminology.belns'


def get_nift_labels() -> Set[str]:
    """Map NIFT names that have been normalized to the original names."""
    bel_resource = get_bel_resource(NIFT_URL)
    return set(bel_resource['Values'])


def main():
    labels = sorted(get_nift_labels())

    df = pd.DataFrame(
        [
            (f'{i:05}', label, '', '', '')
            for i, label in enumerate(labels, start=1)
        ],
        columns=['Identifier', 'Name', 'Type', 'References', 'Description'],
    )
    df.to_csv('terms.tsv', sep='\t', index=False)


if __name__ == '__main__':
    main()
