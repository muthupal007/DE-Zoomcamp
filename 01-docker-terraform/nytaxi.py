import pandas as pd
from sqlalchemy import create_engine
from time import time
import argparse

# print("pandas version: %s" % pd.__version__)

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    database = params.database
    table = params.table
    url = params.url
    # url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-01.csv.gz" 
    # df = pd.read_csv(url, nrows=100)
    # print(len(df))  
    # print(df.head) 
    # taxi_zone = pd.read_csv("https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv")
    # print(len(taxi_zone))
    # print(taxi_zone.head)

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database}")
    # engine.connect()


    df_iter = pd.read_csv(url, chunksize=100000, iterator=True)
    df = next(df_iter)
    df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
    df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
    # print(pd.io.sql.get_schema(df, "green_taxi_data", con=engine))
    # print(df.head(0))
    df.head(0).to_sql(f"{table}", engine, if_exists="replace")
    df.to_sql(f"{table}", engine, if_exists="append")


    for df in df_iter:
        start_time = time() 
        df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
        df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
        df.to_sql(f"{table}", engine, if_exists="append")
        print("Time taken to write 100k rows:", time() - start_time)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Ingest data to postgres")

    parser.add_argument("--user", help="username for postgres")
    parser.add_argument("--password", help="password for postgres")
    parser.add_argument("--host", help="host for postgres")
    parser.add_argument("--port", help="port for postgres")
    parser.add_argument("--database", help="database for postgres")
    parser.add_argument("--table", help="table for postgres")
    parser.add_argument("--url", help="url for data")
    args = parser.parse_args()
    main(args)








