import enum


class BoxStatus(str, enum.Enum):
    open = 'open'
    closed = 'closed'
    done = 'done'


class HelpStatus(str, enum.Enum):
    open = 'open'
    closed = 'closed'
    done = 'done'


class ObjectiveStatus(str, enum.Enum):
    open = 'open'
    closed = 'closed'
    done = 'done'

