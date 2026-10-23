# Spendly - Personal Expense Tracker

## Author

| Roll No. | Name | GitHub username |
|---|---|---|
| 24ESKCS091 | Bhupendra | bhupendrasou |

## About

Spendly is a personal expense tracker web app. Users can add expenses, review
their spending across categories, and read tips and stories about budgeting.
This repository contains the full static site together with the complete
DevOps setup for the course milestones: CI, Docker, deployment, monitoring
and Kubernetes.

## Tech stack

- Frontend: HTML, CSS, JavaScript
- Backend: None (frontend only)
- Database: Browser localStorage (client-side)

## Running locally

```bash
make install
make test
make run        # serves the site on http://localhost:8080
```

## Live URL

[Visit the live Spendly site](https://bhupendrasou.github.io/spendly-live/)

https://bhupendrasou.github.io/spendly-live/

## Health endpoint

`GET /health` returns the running commit SHA, e.g.
`{"status":"ok","commit":"..."}` (served by the container's nginx).

## Container registry

Image: `ghcr.io/skit-devops-2026/devops-24eskcs091:latest`
(built and pushed by the CI workflow on every push to main).

https://github.com/orgs/skit-devops-2026/packages/container/devops-24eskcs091

## Deployment and monitoring

- `docker compose up --build` runs the site (:8080), Prometheus (:9090)
  and Grafana (:3000).
- Kubernetes: `kubectl apply -f k8s/`
- See `docs/deployment.md` for deployment notes and the deployment screenshot.
