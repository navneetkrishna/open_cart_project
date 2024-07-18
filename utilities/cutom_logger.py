import logging
import os


class LogGen:

    @staticmethod
    def loggen():
        log_dir = os.path.join(os.path.abspath(os.curdir), 'logs')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        log_file = os.path.join(log_dir, 'automation.log')

        logger = logging.getLogger('automation_logger')
        logger.setLevel(logging.DEBUG)

        # Create handlers
        file_handler = logging.FileHandler(log_file)
        stream_handler = logging.StreamHandler()

        # Create formatters and add them to handlers
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m%d%y %I %M %S %p')
        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        # Add handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

        return logger

# import logging
# import os
#
#
# class LogGen:
#
#     @staticmethod
#     def loggen():
#         path = os.path.abspath(os.curdir) + '\\logs\\automation.log'
#         # print(path)
#         logging.basicConfig(filename=path,
#                             format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m%d%y %I %M %S %p')
#
#         logger = logging.getLogger()
#         logger.setLevel(logging.DEBUG)
#
#         return logger
