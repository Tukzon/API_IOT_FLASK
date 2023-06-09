
# API IOT Flask

Desarrollo API REST IOT en Flask con SQLite.


## API Reference

### LOCATION
#### Get all locations

```http
  GET /api/v1/location
```

#### Get location by id

```http
  GET /api/v1/location/${id}
```

| Parameter | Type     |
| :-------- | :------- |
| `id`      | `int` |

#### Create location

```http
  POST /api/v1/location
```

| Parameter | Type     |
| :-------- | :------- |
| `location_name`      | `string` |
| `location_country` | `string` |
|  `location_city`| `string` |
|  `location_meta`| `string` |

#### Delete location

```http
  DELETE /api/v1/location/${id}
```

| Parameter | Type     |
| :-------- | :------- |
| `id`      | `int` |

#### Update location

```http
  PUT /api/v1/location/${id}
```

| Parameter | Type     |
| :-------- | :------- |
| `id`      | `int` |
| `location_name`      | `string` |
| `location_country` | `string` |
|  `location_city`| `string` |
|  `location_meta`| `string` |

### SENSOR

#### Create sensor

```http
  POST /api/v1/sensor
```

| Parameter | Type     |
| :-------- | :------- |
| `sensor_name`      | `string` |
| `sensor_category` | `string` |
|  `location_id`| `int` |
|  `sensor_meta`| `string` |

#### Get all sensors

```http
  GET /api/v1/sensor
```

#### Get sensor by API_KEY

```http
  GET /api/v1/sensor/${sensor_api_key}
```

| Parameter | Type     |
| :-------- | :------- |
| `sensor_api_key`      | `string` |

#### Update sensor

```http
  PUT /api/v1/sensor/${sensor_api_key}
```

| Parameter | Type     |
| :-------- | :------- |
| `sensor_api_key`      | `string` |
| `sensor_name`      | `string` |
| `sensor_category` | `string` |
|  `location_id`| `int` |
|  `sensor_meta`| `string` |

#### Delete sensor

```http
  DELETE /api/v1/sensor/${sensor_api_key}
```

| Parameter | Type     |
| :-------- | :------- |
| `sensor_api_key`      | `string` |

### COMPANY

#### Create company

```http
  POST /api/v1/company
```

| Parameter | Type     |
| :-------- | :------- |
| `company_name`      | `string` |