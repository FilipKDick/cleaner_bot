import enum


class ChoreCompletionStatus(enum.Enum):
    SAFE = 'safe'
    SOON = 'soon'
    DUE = 'due'
    OVERDUE = 'overdue'
