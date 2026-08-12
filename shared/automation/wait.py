import time

def wait_until(condition_fn, timeout=10, interval=0.2, on_timeout=None, condition=None):
    """
    Espera até que condition_fn retorne True ou até estourar o timeout.
    """
    start = time.time()

    while time.time() - start < timeout:
        try:
            if condition_fn():
                print(f'condição: {condition} confirmada')
                time.sleep(0.5)
                return True
        except Exception:
            pass

        time.sleep(interval)

    if on_timeout:
        on_timeout()

    raise TimeoutError(f"Timeout aguardando condição: {condition}")