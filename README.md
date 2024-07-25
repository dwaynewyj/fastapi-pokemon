# Pokémon REST API


## Overview

This project implements a REST API for accessing detailed Pokémon information. Built with FastAPI, it connects to the PokeAPI to provide endpoints for retrieving data about Pokémon species and individual Pokémon. This API supports features like pagination, detailed Pokémon information retrieval, and more.


- Author: Dwayne Jang
- Created: 202407241700
- Updated: 202407241759
  
## Features

- **Pokémon Species Endpoint**: Provides a list of Pokémon species with detailed information, including image URLs, colors, habitats, and more. Supports pagination and customizable results.

- **Detailed Pokémon Endpoint**: Retrieves comprehensive details about a specific Pokémon, including abilities, forms, height, weight, moves, and sprites. Allows specification of the number of moves to fetch.
  
- **Health Check Endpoint**: Simple endpoint to verify the API’s availability and health status. Returns a 200 status code with a message.
  
- **Error Handling**: Includes validation and error handling to ensure robust responses and proper management of invalid requests.

## Technical Notes

  1. **API Integration**: Uses PokeAPI v2 to fetch Pokémon data. questionnaires.
  2. **FastAPI Framework**: Provides an efficient and modern way to create REST APIs with built-in validation, error handling, and performance.
  3. **Docker Deployment**: The project includes Docker support for containerization, enabling easy deployment and scaling using AWS ECS and EKS.

## Setup Instructions

- **Python 3.9 or higher**
- **Docker (for containerization)**
- **Docker Compose (for managing multi-container applications)**


## Installation

1. Clone the repository:

    ```shell
    git clone https://github.com/your-username/fastapi-test-project.git
    ```

2. Navigate to the project directory:

    ```shell
    cd fastapi-pokemon
    ```

3. Create a virtual environment:

    ```shell
    python3 -m venv .venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```shell
        .venv/Scripts/activate
        ```

    - On macOS and Linux:

        ```shell
        source .venv/bin/activate
        ```

5. Install the project dependencies:

    ```shell
    pip3 install -r requirements.txt
    ```

## Usage

1. Start the FastAPI dev server:

    ```shell
    fastapi dev main.py
    ```
    or
    ```
    uvicorn app.main:app --reload
    ```

    The server will be running at `http://localhost:8000`.

2. Open your web browser and navigate to `http://localhost:8000/docs` to access the interactive API documentation provided by FastAPI.

## Unit Test

1. Run FastAPI Pytest:

    ```shell
    pytest -v
    ```

## Docker

1. Start the FastAPI dev server:

    ```shell
    docker-compose build
    docker-compose up
    ```

    The server will be running at `http://localhost:3000`.

2. Open your web browser and navigate to `http://localhost:3000/`.

## User Testing

1. Install Postman

2. Test endpoints


## Main Endpoints
- **Request**: GET http://127.0.0.1:8000 
- **Response**: ```{"message": "Welcome to the Pokemon API"}```

## Healthz Endpoints
- **Request**: GET http://127.0.0.1:8000/v1/healthz
- **Response**: ```{"message": "Ok","status": 200}```

## Species Endpoints
- **Request**: GET http://127.0.0.1:8000/v1/species
- **Request**: GET http://127.0.0.1:8000/v1/species?count=10
- **Request**: GET http://127.0.0.1:8000/v1/species?count=10&index=10
- **Response**: 
```
{
    "species": [
        {
            "id": 1,
            "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/001.png",
            "name": "bulbasaur",
            "base_happiness": 50,
            "capture_rate": 45,
            "colors": [
                "green"
            ],
            "growth_rates": [
                "medium-slow"
            ],
            "habitats": [
                "grassland"
            ],
            "is_legendary": "false",
            "egg_groups": [
                "monster",
                "plant"
            ],
            "shapes": [
                "quadruped"
            ]
        },
        ...
    ]
}
```


## Pokemon Endpoints
- **Request**: POST http://localhost:8000/v1/pokemon
- **Request**: GET http://localhost:8000/v1/pokemon/name/bulbasaur
- **Request**: GET http://localhost:8000/v1/pokemon/1
- **Response**: 
```
{
    "name": "bulbasaur",
    "abilities": [
        "overgrow",
        "chlorophyll"
    ],
    "base_experience": 64,
    "forms": [
        "bulbasaur"
    ],
    "height": 7,
    "weight": 69,
    "moves": [
        "razor-wind",
        "swords-dance",
        "cut",
        "bind",
        "vine-whip"
    ],
    "sprites": {
        ...
    }
}
```



