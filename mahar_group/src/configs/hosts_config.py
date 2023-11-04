

API_HOSTS = {
    "test": "http://192.168.1.3:8888/coolsite/wp-json/wc/v3/",
    "dev": "",
    "prod": ""
}

WOO_API_HOSTS = {
    "test": "http://192.168.1.3:8888",
    "dev": "",
    "prod": ""
}

DB_HOSTS = {
    "docker": {
        "test": {
            "host": "host.docker.internal",
            "database": "coolsite",
            "table_prefix": "wp_",
            "port": 8889
        }
    },
    "machine1": {
        "test": {
            "host": "127.0.0.1",
            "database": "coolsite",
            "table_prefix": "wp_",
            "port": 8889
        }
    },
    "prod": {}
}