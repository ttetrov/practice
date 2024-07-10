from enum import Enum


class Global_Error_Messages(Enum):
    WRONG_STATUS_CODE = 'Received status code is not equal to expected'
    WRONG_ELEMENT_COUNT = 'Number of items is not equal to expected'
