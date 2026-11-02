import re
import sys

from google.api_core.exceptions import NotFound
from google.cloud.bigquery import Client


def main(prefixes):
    client = Client()

    pattern = re.compile("|".join("^{}.*$".format(prefix) for prefix in prefixes))

    ds_items = list(client.list_datasets())
    for dataset in ds_items:
        ds_id = dataset.dataset_id
        if pattern.match(ds_id):
            print("Deleting dataset: {}".format(ds_id))
            try:
                client.delete_dataset(dataset.reference, delete_contents=True)
            except NotFound:
                print("   NOT FOUND")


if __name__ == "__main__":
    main(sys.argv[1:])
