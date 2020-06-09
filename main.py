from custom_logger import CustomLogger
from kpis import kpi_producer


def main():
    port = 80
    logger = CustomLogger()
    logger.logger.info("Running app on port: %i" % port)
    kpi_producer.run(
        host='0.0.0.0',
        port=80,
        debug=True
    )


if __name__ == "__main__":
    main()