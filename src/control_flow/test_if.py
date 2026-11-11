"""IF statement

@see: https://docs.python.org/3/tutorial/controlflow.html

There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is
short for ‘else if’, and is useful to avoid excessive indentation.

An if … elif … elif … sequence is a substitute for the switch or case statements found
in other languages.
"""


def test_if_statement():
    """IF statement"""

    number = 15
    conclusion = ''

    if number < 0:
        conclusion = 'Number is less than zero'
    elif number == 0:
        conclusion = 'Number equals to zero'
    elif number < 1:
        conclusion = 'Number is greater than zero but less than one'
    else:
        conclusion = 'Number bigger than or equal to one'

    assert conclusion == 'Number bigger than or equal to one'


def test_if_multiple_elif_branches():
    """IF statement with several ELIF branches

    Python checks the conditions from top to bottom and runs only the first branch whose
    condition is true, so the order of the branches matters.
    """

    def describe_temperature(temperature):
        if temperature < 0:
            description = 'Freezing'
        elif temperature < 10:
            description = 'Cold'
        elif temperature < 20:
            description = 'Mild'
        elif temperature < 30:
            description = 'Warm'
        else:
            description = 'Hot'

        return description

    # -5 is also less than 10, 20 and 30, but only the first true branch runs.
    assert describe_temperature(-5) == 'Freezing'
    # 0 is not less than 0, so it falls through to the next branch.
    assert describe_temperature(0) == 'Cold'
    assert describe_temperature(15) == 'Mild'
    assert describe_temperature(25) == 'Warm'
    assert describe_temperature(35) == 'Hot'
