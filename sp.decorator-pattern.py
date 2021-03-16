#!/usr/bin/env python

"""
Structural Pattern --> Decorator Pattern

This pattern is used to extend functionality of existing class by wrapping it up with decorator class/method
"""
from functools import wraps

def wlecome_email_to_customer(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        # module to send email
        return (f"Mail sent with the subject--> Welcome onboard {fn(*args, **kwargs)}")
    return wrapped

@wlecome_email_to_customer
def register_customer(customer_name):
    return customer_name

if __name__ == '__main__':
    print (register_customer("John Doe"))

