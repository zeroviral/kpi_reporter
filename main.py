from reminders import logger
from reminders import reminders_producer


def main():
    port = 5000
    logger.info("Running app on port: %i" % port)
    reminders_producer.run(
        # '0.0.0.0' Allows to be access externally
        host='0.0.0.0',
        debug=True
    )


if __name__ == "__main__":
    main()
