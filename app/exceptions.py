class SeatNumberError(ValueError):
    pass

class MatchIdError(ValueError):
    pass

class MatchNameError(ValueError):
    pass

class UsernameError(ValueError):
    pass

class StadiumNotExistError(ValueError):
    pass

class StadiumExistError(ValueError):
    pass

class SeatNotAvailable(ValueError):
    pass

class BalanceError(ValueError):
    pass

class SaveCacheServerError(RuntimeError):
    pass

class NotAuthorizedUserError(PermissionError):
    pass