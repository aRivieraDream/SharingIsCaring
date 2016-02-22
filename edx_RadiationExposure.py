def radiationexposure(start, stop, step):
    if start >= stop:
        return float(0)
    else:
        return (f(start) * step) + radiationexposure(start + step, stop, step)