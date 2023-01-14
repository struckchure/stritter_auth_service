from config.db import db


def on_startup() -> None:
    db.connect()


def on_shutdown() -> None:
    if not db.is_closed():
        db.close()
