

"""
    Understand:
        + Input:
        + Output:

        Plan:
            +


"""
from icmplib import ping


def run():
    ip = '10.240.21.160'
    print(ping(ip, count=4, interval=1, timeout=2, id=None, source=None, family=None, privileged=False))


if __name__ == "__main__":
    run()
