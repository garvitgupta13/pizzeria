# Pizzeria Project

Welcome to the Pizzeria repository!

This project a simple example of implementing message queue system in a django application. It uses both tradational and message queue to process orders.

## Installation

To set up the project, follow these steps:

1. Redis

    ```bash
    sudo apt-get install redis
    redis-server --daemonize yes
    redis-cli ping
    ## PONG
    ```

2. Repository

    ```bash
    git clone https://github.com/garvitgupta13/pizzeria.git
    cd pizzeria
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver
    ```

3. Run worker threads to process those orders (you can run multiple workers in different terminals), ensure redis is running

    ```bash
    rq worker -c app.settings --with-scheduler
    ```

4. Run RQ Dashboard to monitor the worker threads

    ```bash
    rq-dashboard
    ```

## Usage

There are two endpoints to create orders:

1. [**POST**] `/order/bulk-create/`
2. [**POST**] `/order/enqueue/`

Hit the above endpoints with payload `{"order_cnt": 10}` to create 10 orders.

First endpoint will linearly process the orders and return the response after creating all the orders.

Second endpoint will push the orders to the message queue and return response while the worker threads will process them in background.
