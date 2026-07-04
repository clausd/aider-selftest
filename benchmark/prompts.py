instructions_addendum = """
####

Use the above instructions to modify the supplied files: {file_list}
Don't change the names of existing functions or classes, as they may be referenced from other code like unit tests, etc.
Only use standard libraries, don't suggest installing any packages.
"""  # noqa: E501


test_failures = """
####

See the testing errors above.
The tests are correct, don't try and change them.
Fix the code in {file_list} to resolve the errors.
"""


# Fed back to the model between dryrun iterations. The output is from the
# STRIPPED test file (opaque test names, no assertions) so the model only sees
# compile / runtime errors from its own code, not oracle expected values.
dryrun_feedback = """
####

The stripped test suite reported the errors above. These are compile / runtime
errors from running your code against smoke tests (no expected-value
assertions — test names are opaque). Fix the code in {file_list} so that all
smoke tests run to completion without errors. Do not try to guess the expected
outputs; focus only on making the code compile and run without crashing.
"""
