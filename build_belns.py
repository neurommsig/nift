# -*- coding: utf-8 -*-

import json
from typing import Mapping, Optional

import pandas as pd
from bel_resources import write_namespace
from bel_resources.constants import NAMESPACE_DOMAIN_OTHER


def _write_namespace(path, values: Mapping[str, str], namespace_version: Optional[str] = None):
    with open(path, 'w') as file:
        write_namespace(
            namespace_name='Neuroimaging Feature Terminology',
            namespace_keyword='NIFT',
            namespace_domain=NAMESPACE_DOMAIN_OTHER,
            namespace_version=namespace_version,
            author_name='Sepehr Golriz',
            author_contact='sepehr.golriz.khatami@scai-extern.fraunhofer.de',
            values=values,
            author_copyright='CC0 1.0 Universal',
            case_sensitive=True,
            cacheable=True,
            file=file,
        )


def main():
    df = pd.read_csv('terms.tsv', sep='\t', dtype={'Identifier': str})

    # FIXME use classes.tsv for annotations
    _write_namespace(
        path='nift.belns',
        values={
            identifier: 'OGRPBCAM'
            for identifier in df['Identifier']
        }
    )

    _write_namespace(
        path='nift-names.belns',
        values={
            identifier: 'OGRPBCAM'
            for identifier in df['Name']
        }
    )

    with open('nift.belns.mapping', 'w') as file:
        json.dump(
            dict(df[['Identifier', 'Name']].values),
            file,
            indent=2,
        )


if __name__ == '__main__':
    main()
