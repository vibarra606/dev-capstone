# dev-capstone
Capstone project for CIS 3353

## Attack container status (2026-10-25)

- Container builds and runs via `docker compose up -d --build`.
- Loads correctly at `http://localhost:8080` on the host machine.
- VM cannot reach `http://192.168.56.1:8080` — times out.
- Suspected cause: Windows Firewall or the VirtualBox adapter's network profile (Public vs Private) on the host.
- Next step: set the VirtualBox Host-Only adapter to Private, or add an explicit inbound firewall rule for port 8080.