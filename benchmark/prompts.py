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


# ---- Research + plan phase (feeds an external Perplexity search tool) ----

research_question_generator = """
You are about to solve a programming exercise. Before writing any code, you may
consult a general web search engine. Emit between 1 and 3 SHORT search queries
(one per line, each prefixed with "QUERY: ") that would help you understand
the algorithms, standard library APIs, or common patterns you might need.

Rules for your queries:
- Do NOT include the words: test, assert, expected, exercism, solution, kata.
- Do NOT ask for the specific answer, expected output, lyrics, or reference
  solution — the queries must be about general concepts, algorithms, or APIs.
- Do NOT include the exercise name.
- Focus on generic knowledge you'd look up in official docs or StackOverflow.
- Keep each query under 12 words.

The exercise description is below.

---

{instructions}

---

Emit only the QUERY lines; no other text.
"""


research_plan_prompt = """
Below are the raw web-search results for the queries you asked. Use them to
inform your understanding, but remember: the results are general references,
not the specific solution.

--- Search results ---

{findings}

--- Task ---

Now write a concise, numbered plan (5 to 10 steps) for implementing the
exercise. Do NOT write any code yet — just the plan. The plan will be used to
guide the actual coding step immediately afterwards.
"""


research_context_header = """
####

# Research findings + plan (from a prior research phase)

The following was gathered in a research + planning phase before you started
writing code. Use it as reference material; when in doubt, prefer the actual
problem statement above.
"""


# ---- strict-types mode (--strict-types) ----

strict_types_addendum = """
####

# Strict-types mode

Your solution must satisfy strict static type checking:

- **Python**: pass `mypy --strict`. Every function signature (parameters and
  return type) must be fully annotated. Do not use `typing.Any`. Prefer
  precise generics (e.g. `list[int]`, `dict[str, int]`).
- **JavaScript**: pass `tsc --allowJs --checkJs --strict --noEmit`. Every
  exported function must have JSDoc parameter and return type annotations
  (e.g. `@param {number} x`, `@returns {string[]}`).

Do not change the public function or class names or the number/order of their
parameters — the test suite is untouched from the baseline benchmark and
depends on those identifiers.

Static type errors will be reported before test failures. Fix type errors
first, then test failures.
"""


strict_types_feedback_header = """
####

# Static type errors (fix these first)

The static type checker reported the errors below. Fix them before making
further changes to the solution's runtime behavior. The tests were not run
this iteration because the code did not type-check.
"""


# ---- Critique + revise cycle (--critique-cycles) ----

critique_prompt = """
####

Now take a critical second look at your solution above.

Compare it line-by-line against the problem statement (the original instructions
at the top of this conversation). List every place where your code might
diverge from what the spec requires:

- edge cases the spec mentions that your code does not visibly handle
- constraints or invariants the spec states that your code does not enforce
- specific wording in the spec that does not clearly map to a line of your code
- outputs, formatting, or exceptions the spec calls for that your code produces
  differently

Do NOT restate the spec. Do NOT rewrite the code. Just enumerate the concerns
you have about your own code, one per bullet. Be concrete: reference the
specific spec phrase and the specific line of your code you are worried about.

Emit only the bulleted list of concerns and nothing else — no code, no fences,
no revised solution.
"""


revise_prompt = """
####

Now rewrite the solution to address the specific concerns you listed above.

Rules:
- Only fix issues you called out. Do not add features, options, or handling
  the spec does not ask for.
- Do not weaken or work around any test the spec implies.
- Keep the public interface (function or class names, parameter names, return
  shape) exactly as it is.
- Emit only the updated solution file(s) in the standard fenced-code format.
"""
