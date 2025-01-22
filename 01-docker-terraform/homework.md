# Homework Answers

## 1. 
    docker run -it --entrypoint bash python:3.12.8
    pip --version

## 2.
    docker compose up
    (Register new server in pgadmin UI to verify hostname and port)

## 3.
    
    SELECT count(*) FROM public.green_taxi_oct19
    where 
    lpep_pickup_datetime >= '2019-10-01 00:00:00' and   lpep_dropoff_datetime < '2019-11-01 00:00:00'
    and trip_distance <= 1

    SELECT COUNT(*)
    FROM public.green_taxi_oct19
    WHERE 
        lpep_pickup_datetime >= '2019-10-01' 
        AND lpep_dropoff_datetime < '2019-11-01'
        AND trip_distance > 1 
        AND trip_distance <= 3;

    SELECT COUNT(*)
    FROM public.green_taxi_oct19
    WHERE 
        lpep_pickup_datetime >= '2019-10-01' 
        AND lpep_dropoff_datetime < '2019-11-01'
        AND trip_distance > 3 
        AND trip_distance <= 7;

    SELECT COUNT(*)
    FROM public.green_taxi_oct19
    WHERE 
        lpep_pickup_datetime >= '2019-10-01' 
        AND lpep_dropoff_datetime < '2019-11-01'
        AND trip_distance > 7 
        AND trip_distance <= 10;

    SELECT COUNT(*)
    FROM public.green_taxi_oct19
    WHERE 
        lpep_pickup_datetime >= '2019-10-01' 
        AND lpep_dropoff_datetime < '2019-11-01'
        AND trip_distance > 10;

## 4.
    SELECT DATE(lpep_pickup_datetime)
    FROM public.green_taxi_oct19
    WHERE DATE(lpep_pickup_datetime) IN ('2019-10-11', '2019-10-24',    '2019-10-26', '2019-10-31')
    ORDER BY trip_distance DESC
    LIMIT 1;

## 5.
    SELECT SUM(t.total_amount) as "TotalAmountAllTrips", 
    		z."Zone" 
    FROM public.green_taxi_oct19 t 
    JOIN taxi_zone_lookup z
    ON t."PULocationID" = z."LocationID"
    WHERE DATE(t.lpep_pickup_datetime) = '2019-10-18'
    GROUP BY z."Zone"
    ORDER BY "TotalAmountAllTrips" DESC
    LIMIT 3

## 6.
    SELECT zd."Zone"
    FROM public.green_taxi_oct19 t 
    JOIN taxi_zone_lookup zp
    ON t."PULocationID" = zp."LocationID"
    JOIN taxi_zone_lookup zd
    ON t."DOLocationID" = zd."LocationID"
    WHERE zp."Zone" = 'East Harlem North'
    ORDER BY t.tip_amount DESC
    LIMIT 1

## 7.
    terraform init
    terraform apply -auto-approve
    terraform destroy


