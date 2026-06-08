## Projeto MATA52

### Algoritmos utilizados

Módulo `services/schedule_resolver.py` — dois algoritmos para escolher atividades sem sobreposição de horário:

- **`greedy_classic`** — guloso clássico: ordena por fim, aceita atividade se não conflita com as já escolhidas. Maximiza quantidade de atividades. [Referência](https://www.geeksforgeeks.org/dsa/activity-selection-problem-greedy-algo-1/#expected-approach-1-using-sorting-on-logn-time-and-on-space)
- **`dp_weighted`** — programação dinâmica: maximiza peso total (`prioridade + participantes/5`). [Referência](https://www.geeksforgeeks.org/dsa/weighted-job-scheduling/)

Ambos retornam `(atividades_selecionadas, tempo_ms)`.

### Como rodar

Requisitos:

- Python 3.12+
- `uv` (https://docs.astral.sh/uv/)

```bash
uv sync
uv run flask --app main run
```

Abra [http://127.0.0.1:5000](http://127.0.0.1:5000).

Sem `uv`:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
flask --app main run
```
