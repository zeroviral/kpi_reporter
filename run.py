from reminders import logger
from reminders import reminders_app


def run():
    port = 5000
    logger.info("Running app on port: %i" % port)
    reminders_app.run(
        # '0.0.0.0' Allows to be access externally
        host='0.0.0.0',
        port=80,
        debug=True
    )


if __name__ == "__main__":
    run()
