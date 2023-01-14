import importlib
import inspect
import pkgutil

import peewee
import typer
import uvicorn

from config import db, env

typer_app = typer.Typer()


def get_models():
    model_files = [
        f"models.{name}" for _, name, _ in pkgutil.iter_modules(["src/models"])
    ]

    for model in model_files:
        for _, obj in inspect.getmembers(importlib.import_module(model)):
            if (
                inspect.isclass(obj)
                and obj.__name__ != "BaseModel"
                and isinstance(obj, peewee.ModelBase)
            ):
                yield obj


@typer_app.command()
def migrate():
    db.db.connect()
    db.db.create_tables(models=list(get_models()))


@typer_app.command()
def drop():
    db.db.connect()
    db.db.drop_tables(models=list(get_models()))


@typer_app.command()
def run_server(host="0.0.0.0", port=env.API_PORT):
    uvicorn.run(
        "config.app:app",
        host=host,
        port=int(port),
        reload=True,
    )


def main():
    typer_app()


if __name__ == "__main__":
    main()
