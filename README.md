# Luigid docker image

Centralized luigi instance

`<IP>:8082`

Configure your runs to use the instance on `<IP>:8082` with your `luigi.cfg` config

## Run image

```shell
docker-compose up -d
```

## Run test

```shell
rm -rf /tmp/luigi_test && \
mkdir -p /tmp/luigi_test && \
python -m luigi --module test RootOfAllBananas --workers=3
```

