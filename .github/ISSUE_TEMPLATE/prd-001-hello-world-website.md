# [Feature] Hello World Website (PRD-001)

**Labels:** `feature`, `good-first-issue`  
**Priority:** P0  

---

## Description

Create the first website for `my-repo` — a minimal "Hello, World!" HTML page served via Python's built-in HTTP server. This validates the full multi-agent GitOps pipeline and establishes project conventions.

## PRD Reference

See [PRD-001: Hello World Website](./docs/prds/PRD-001-hello-world-website.md)

## Requirements

### Implementation Details

Create the following files:

**`index.html`** — Main HTML page:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hello, World!</title>
</head>
<body>
  <h1>Hello, World!</h1>
  <p>Welcome to my-repo!</p>
</body>
</html>
```

**`run.sh`** — One-command launcher:
```bash
#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 -m http.server 8080 --bind 127.0.0.1
```

**`README.md`** — Project documentation with:
- Description
- Prerequisites (Python 3)
- Quick Start: `chmod +x run.sh && ./run.sh`
- Project structure overview

**`.gitignore`** — Standard ignores:
```
__pycache__/
*.pyc
.DS_Store
venv/
.env
```

## Acceptance Criteria

- [ ] `index.html` exists at project root with "Hello, World!" in `<h1>`
- [ ] `run.sh` exists and is executable (`chmod +x run.sh`)
- [ ] `README.md` exists with Description, Quick Start, and Project Structure sections
- [ ] `.gitignore` exists with appropriate entries
- [ ] Running `./run.sh` starts a web server on `http://127.0.0.1:8080`
- [ ] `curl http://127.0.0.1:8080` returns HTTP 200 with HTML containing "Hello, World!"

## Developer Instructions

1. Create branch: `feature/prd-001-hello-world-website`
2. Create the four files listed above
3. Commit with message: `feat: create hello world website (PRD-001)`
4. Push branch and open a Pull Request
5. Title the PR: `[Feature] Hello World Website (PRD-001)`

## Notes for Reviewer

- Verify `index.html` uses semantic HTML5 tags
- Check `run.sh` has `set -euo pipefail` and binds to `127.0.0.1` (not `0.0.0.0`)
- Confirm no external dependencies are introduced
- Ensure `.gitignore` covers OS-specific files

## Notes for Tester

- Run `./run.sh` and verify the server starts without errors
- In another terminal, run `curl http://127.0.0.1:8080` and confirm HTTP 200
- Verify the HTML contains both "Hello, World!" and "Welcome to my-repo!"
- Kill the server with Ctrl+C after testing
