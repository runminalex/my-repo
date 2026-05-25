## Description

Create the first website for `my-repo` — a minimal "Hello, World!" HTML page served via Python's built-in HTTP server. This validates the full multi-agent GitOps pipeline and establishes project conventions.

## PRD Reference

See [PRD-001: Hello World Website](./docs/prds/PRD-001-hello-world-website.md)

## Acceptance Criteria

- [ ] `index.html` exists at project root with "Hello, World!" in `<h1>`
- [ ] `run.sh` exists and is executable (`chmod +x run.sh`)
- [ ] `README.md` exists with Description, Quick Start, and Project Structure sections
- [ ] `.gitignore` exists with appropriate entries
- [ ] Running `./run.sh` starts a web server on `http://127.0.0.1:8080`
- [ ] `curl http://127.0.0.1:8080` returns HTTP 200 with HTML containing "Hello, World!"

## Developer Instructions

1. Create branch: `feature/prd-001-hello-world-website`
2. Create `index.html`, `run.sh`, `README.md`, and `.gitignore`
3. Commit with message: `feat: create hello world website (PRD-001)`
4. Push branch and open a Pull Request with title `[Feature] Hello World Website (PRD-001)`

## Notes for Reviewer

- Verify `index.html` uses semantic HTML5 and valid structure
- Check `run.sh` uses `set -euo pipefail` and binds to `127.0.0.1`
- Confirm zero external dependencies
- Ensure `.gitignore` covers OS-specific files

## Notes for Tester

- Run `./run.sh` and verify the server starts
- `curl http://127.0.0.1:8080` should return HTTP 200 with "Hello, World!" in the body
- Verify both "Hello, World!" and "Welcome to my-repo!" are present in the HTML
