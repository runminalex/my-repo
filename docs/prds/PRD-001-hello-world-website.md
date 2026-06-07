# PRD-001: Hello World Website

## Status
Approved

## Goal
Create a simple "Hello, World!" static website served via Python's built-in HTTP server.

## Requirements
1. A single `index.html` page displaying "Hello, World!"
2. Server using Python 3's built-in `http.server` module
3. Simple one-command launch script
4. No external dependencies

## Success Criteria
- Running `./run.sh` starts the server on `http://127.0.0.1:8080`
- Opening the URL shows a webpage with "Hello, World!" greeting
- Server stops cleanly with Ctrl+C
