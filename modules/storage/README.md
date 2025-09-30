Here are some SQL commands that will give you a jump start on what needs to be done with the RDS cluster. 
These values are from the datasets from the OpenSky Network https://zenodo.org/record/5377831, but can be updated based on which dataset you choose to use.
You do not have to use these commands verbatum, they're just meant to assist with the database side of things. You can go about it any way you see fit to accomplish the goal.

```
	CREATE TABLE IF NOT EXISTS traffic_data (
		callsign VARCHAR(10),
		number VARCHAR(10),
		icao24 VARCHAR(10),
		registration VARCHAR(20),
		typecode VARCHAR(10),
		origin VARCHAR(10),
		destination VARCHAR(10),
		firstseen TIMESTAMP,
		lastseen TIMESTAMP,
		day DATE,
		latitude_1 DECIMAL(10,8),
		longitude_1 DECIMAL(11,8),
		altitude_1 FLOAT,
		latitude_2 DECIMAL(10,8),
		longitude_2 DECIMAL(11,8),
		altitude_2 FLOAT
	);
```
```
  CREATE TABLE IF NOT EXISTS traffic_summary (
      id INT PRIMARY KEY,
      row_count INT,
      last_transponder_seen_at TIMESTAMP,
      most_popular_destination VARCHAR(10),
      count_of_unique_transponders INT
  );
```
```
  INSERT INTO traffic_data (
      callsign, number, icao24, registration, typecode, origin, destination,
      firstseen, lastseen, day, latitude_1, longitude_1, altitude_1, latitude_2, longitude_2, altitude_2
  ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
```
```
  SELECT COUNT(*) FROM traffic_data
```
```
  SELECT MAX(lastseen) FROM traffic_data
```
```
  SELECT destination, COUNT(*) as count
  FROM traffic_data
  WHERE destination IS NOT NULL AND destination != ''
  GROUP BY destination
  ORDER BY count DESC
  LIMIT 1
```
```
  SELECT COUNT(DISTINCT icao24) FROM traffic_data
```
```
      INSERT INTO traffic_summary (id, row_count, last_transponder_seen_at, most_popular_destination, count_of_unique_transponders)
      VALUES (1, %s, %s, %s, %s)
      ON DUPLICATE KEY UPDATE
          row_count = VALUES(row_count),
          last_transponder_seen_at = VALUES(last_transponder_seen_at),
          most_popular_destination = VALUES(most_popular_destination),
          count_of_unique_transponders = VALUES(count_of_unique_transponders)
  """, (
      row_count,
      last_transponder_seen_at,
      most_popular_destination,
      count_of_unique_transponders
  )
```
```
  SELECT * FROM traffic_summary WHERE id = 1
```
