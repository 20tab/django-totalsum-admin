twentytab-totalsum-admin
========================

A django app that initializes admin changelist view with last row in results as sum of some numerical fields or properties

## Installation

Use the following command: <b><i>pip install twentytab-totalsum-admin</i></b>

## Configuration

- settings.py

```py
INSTALLED_APPS = {
    ...,
    'totalsum',
    ...
}
```


## Usage

```py
from totalsum.admin import TotalsumAdmin


class MyAdmin(TotalsumAdmin):
    totalsum_list = ('model_field1', 'model_field2', 'model_property')
    unit_of_measure = '&euro;'
```


