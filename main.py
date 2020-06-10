from reminders.custom_logger import CustomLogger
from reminders import reminders_producer


def main():
    port = 80
    logger = CustomLogger()
    logger.logger.info("Running app on port: %i" % port)
    reminders_producer.run(
        host='0.0.0.0',
        port=80,
        debug=True
    )


if __name__ == "__main__":
    main()
