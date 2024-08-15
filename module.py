# pi = 4.6567
# clear=lambda: print("\033c", end='', flush=True)

import sys
def clear_line():
    sys.stdout.write('\r' + ' ' * 80 + '\r')
    sys.stdout.flush()


