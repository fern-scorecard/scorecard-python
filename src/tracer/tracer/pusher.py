import logging
from threading import Thread

from tracer.database import LogRecord, Table

# eventually we will want to replace this and log to Scorecard directly
# that should be fine by implementing a custom log handler.
# that writes to a url endpoint.
# I'll probably take a dependency on the sdk for this.
# I dunno yet tbh.
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    filename=f'tracer.log')
logger = logging.getLogger(__name__)
logRecordTable = Table(LogRecord)


# this is a naive implementation and really we should have a background process that fluses the logs to scorecard
# periodically. But this is just to demonstrate the concept.
class LogPusher(Thread):
    def __init__(self, data: LogRecord):
        super(LogPusher, self).__init__()
        self.data = data

    def run(self):
        logger.debug(f"Pushing {self.data.model_dump_json()} to Scorecard")
        # TODO(pfbyjy): Log to Scorecard here instead of
        # writing to a file.
        logger.debug(self.data.model_dump_json())
        logRecordTable.sync_insert_no_check(self.data)
