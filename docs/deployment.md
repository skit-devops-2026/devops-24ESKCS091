# Deployment - Spendly (24ESKCS091)

- Live URL: https://bhupendrasou.github.io/spendly-live/
- The organisation repository cannot enable GitHub Pages without an admin
  (Settings -> Pages is restricted and the deployment workflow's
  configure-pages step fails with "Resource not accessible by integration"),
  so the site is deployed from the author's personal repository
  https://github.com/bhupendrasou/spendly-live (GitHub Pages, Deploy from a
  branch: main, / root). The screenshot of the live site is
  docs/deployment-screenshot.png.
- Container image: ghcr.io/skit-devops-2026/devops-24eskcs091:latest
  (built and pushed by the CI workflow on every push to main).

## Local deployment with Docker

```bash
docker compose up --build
# site:        http://localhost:8080
# health:      http://localhost:8080/health
# Prometheus:  http://localhost:9090
# Grafana:     http://localhost:3000
```

## Kubernetes

```bash
kubectl apply -f k8s/
```
