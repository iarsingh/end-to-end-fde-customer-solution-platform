class InputError(ValueError):
    pass


def check(body):
    if not isinstance(body, dict):
        raise InputError("body must be an object")
    failed = []

    for key in ("constraint", "metric", "shadow_week", "readout"):
        if not body.get(key): failed.append(key)
    return {"passed": not failed, "failed": failed, "applied": False}
