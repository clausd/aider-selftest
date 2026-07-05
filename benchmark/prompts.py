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


# Shown to the model at the start of a selftest-mode exercise. The test file
# is added to the model's editable set; the model is asked to author its own
# assertions verifying its solution.
selftest_setup = """
####

This exercise runs in SELFTEST mode. You will implement the solution AND
author your own tests for it in {test_file_list}.

The test file(s) currently contain a stripped skeleton showing the exact
inputs the grader will use, but with:
- opaque test names (test_case_001, testCase001, etc.)
- assertion arguments redacted (only the call to your code remains)

Your task:
1. Implement the solution in {file_list}
2. For each test_case in the test file, ADD assertions verifying what you
   believe the correct behavior should be for that input. Do not rename the
   test methods, remove existing calls, or change the input arguments.

Only edit these files. The stripped structure of the test file is what the
grader expects — augment it with your assertions, don't restructure it.
"""


# Fed back to the model between selftest iterations when its own assertions
# reject its solution.
selftest_feedback = """
####

Your own assertions in {test_file_list} rejected your current solution. The
test output is above. Reconcile the two: either the solution is wrong, or
your assertions encode a wrong understanding of the spec — decide which and
fix it. Update {file_list} accordingly.
"""
