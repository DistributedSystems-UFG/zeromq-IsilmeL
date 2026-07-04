[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wa7oHGos)
# ZeroMQ-Examples
Examples extracted from Tanenbaum&vanSteen (2025) to illustrate three different communication patterns with ZeroMQ: client-server, pub-sub and producer-consumer.

## Alterações
Cada exemplo roda em processos separados, um por máquina (edite os IPs em `constPipe.py`).

- **client-server**: `server.py` / `client.py <IP>`. Novo: comandos `UPPER`, `REV`, `COUNT`.
- **pub-sub**: `publisher.py` / `subscriber.py <IP>`. Novo: tópico `TEMP`.
- **pipeline**: `tasksrc.py 1|2` → `taskmid.py` (novo estágio, dobra o valor) → `taskwork.py`.
