This code was forked from [this repository](https://github.com/simon-larsson/pokemon-name-generator) and the model is used to serve a REST API endpoint.

# Pokémon Name Generator

Generates new unique Pokemon names with Keras using a recurrent neural network (LSTM). Written as a generic text generator that can be used to generate lines of poetry, other names, or just text in general. It all depends on what it gets input.

[Notebook with code and explainations](https://github.com/simon-larsson/pokemon-name-generator/blob/master/name_generator.ipynb)

## Sample Pokémon Names

|               |               |               |               |
| ------------- | ------------- | ------------- | ------------- |
| Purndew       | Chingoos      |  Nodow        |  Fregaycha    |
| Magmagly      | Cteenidel     |  Browodon     |   Noinga      |
| Ferfeon       | Midgeos       |  Deowwar      |   Harouthal   |
| Spera         | Kleffas       |  Picorno      |   Suorthe     |
| Ponytau       | Jellpid       |  Mewable      |  Meetty       |
| Phound        | Passir        |  Golduzon     |  Frislask     |
| Carmados      | Hidgeosta     |  Turtyken     |  Durmast      |
| Iscullink     | Glagant       |  Togices      |   Graggeon    |
| Bouhiganix    | Sawio         |  Dragonib     |  Tohurk       |
| Zwinauk       | Grodosell     |   Woorat      | Lempole       |


## Installation (without Docker)
Install all the dependencies.
```bash
pip3 install -r requirements.txt
```

Start the API
```bash
python3 api/api.py
```


## Installation with Docker
Build the Docker container.
```bash
docker build -t name-generator .
```

Run the docker container and map the internal port to external port-
```bash
docker run -p 5000:5000/tcp name-generator
```

## Access API
### With Swagger
Go to [http://localhost:5000/swagger/](http://localhost:5000/swagger/) to use the interactive Swagger documentation.

### Endpoint
Make a `GET`-request to [http://localhost:5000/names?amount=3](http://localhost:5000/names?amount=3) and specify the amount as a string parameter (default=1).
