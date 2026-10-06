# devops-starter

### how to improve my workflow

1. Split into separate jobs
   problem: In a single job, steps run one after another. If tests fail, the security scan never runs, so I will only learn about one problem at a time

so each job gets its own runner and they run in parallel by default

jobs:
test:
security:

- Faster overall, and a failure points straight at test or security.
- Each job starts empty, so it repeats checkout, Python setup, and install.

2. Avoid duplicate runs

Problem: With plain push: and pull_request:, pushing to a branch that has an open PR triggers the workflow twice: once for the push, once for the PR update.

Fix:

yaml
on:
push:
branches: [main]
pull_request:
branches: [main]

- Pushes to main are tested after merge.
- Feature-branch changes are tested through the PR only.

3. Tune Bandit

Problem: bandit -r . flags every assert in your test file as B101 (assert_used). In tests, assert is how pytest works, so this is noise. The step may go red for no real reason.

Fix: bandit -r . -x ./test_calculator.py,./.venv -ll

Flag Meaning
-r . scan recursively from the current directory
-x path1,path2 exclude files or folders (tests, virtual environments)
-l / -ll / -lll report only low+ / medium+ / high severity

- Developers trust a scanner that reports real issues. Constant false alarms train people to ignore it.
- Don't over-filter. Excluding tests is sensible, but suppressing real findings defeats the purpose. Use # nosec on individual lines only with a justification.
