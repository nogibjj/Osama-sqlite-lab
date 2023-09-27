# """
# ETL-Query script
# """

# from mylib.extract import extract
# from mylib.transform_load import load
# from mylib.query import query

# # Extract
# print("Extracting data...")
# extract()

# # Transform and load
# print("Transforming data...")
# load()

# # Query
# print("Querying data...")
# query()

# """
# ETL-Query script
# """

import argparse
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query


def main(args):
    # Extract
    print("Extracting data...")
    extract()

    # Transform and load
    print("Transforming data...")
    load()

    # Query
    if args.query:
        print("Querying data...")
        query()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ETL-Query script")
    parser.add_argument("--query", action="store_true", help="query the database")
    args = parser.parse_args()
    main(args)