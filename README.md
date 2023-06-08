
# API IOT Flask

Desarrollo API REST para IOT en Flask Para Arquitecturas Emergentes.


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

#### EN CONSTRUCCIÓN