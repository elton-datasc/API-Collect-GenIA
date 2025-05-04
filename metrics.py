
import csv
from datetime import datetime

def salvar_metricas(metricas, path="metricas.csv"):
    metricas["timestamp"] = datetime.now().isoformat()
    with open(path, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=metricas.keys())
        if f.tell() == 0:
            writer.writeheader()
        writer.writerow(metricas)
