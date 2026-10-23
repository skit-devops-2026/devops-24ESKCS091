# Monitoring - Spendly

- `prometheus.yml` - Prometheus scrape configuration (Prometheus itself and
  the nginx-prometheus-exporter for the Spendly container).
- `dashboard.json` - Grafana dashboard "Spendly - Nginx Overview". Also
  provisioned automatically under `grafana/` for the docker compose stack.

Run the full stack with `docker compose up --build`:
site on :8080, Prometheus on :9090, Grafana on :3000 (admin/admin).
