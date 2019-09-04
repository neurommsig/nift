# -*- coding: utf-8 -*-

import pandas as pd
import requests
from tqdm import tqdm

GILDA_URL = 'http://34.201.164.108:8001'


def post_gilda(text: str, url: str = GILDA_URL) -> requests.Response:
    """Send text to GILDA."""
    return requests.post(f'{url}/ground', json={'text': text})


def main() -> None:
    xrefs_df = pd.read_csv('xrefs.tsv', sep='\t', dtype={'Identifier': str})
    previous_nift_ids = set(xrefs_df['Identifier'])

    terms_df = pd.read_csv('terms.tsv', sep='\t', dtype={'Identifier': str})
    it = tqdm(terms_df.values, desc='Searching Gilda')
    for nift_id, label, nift_type, xrefs, description in it:
        if nift_id in previous_nift_ids:  # skip already xref'd terms
            continue

        res = post_gilda(label)
        results = res.json()
        if not results:
            continue

        for result in results:
            it.write('\t'.join((
                nift_id,
                label,
                result['term']['db'],
                result['term']['id'],
                result['term']['entry_name'],
            )))


if __name__ == '__main__':
    main()
