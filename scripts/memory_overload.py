import time
import numpy as np

memory_blocks = []
allocation_size = 100_000_000  # Aloca  100 MB por segundo
duration = 20 # Executa por 20 segundos

for second in range(1, duration + 1):
    try:
        memory_blocks.append(np.ones((allocation_size,), dtype=np.uint8))
        allocated_gb = (second * allocation_size) / (1024 ** 3)
        print(f"Tempo {second}s - Memória alocada: {allocated_gb:.2f} GB")
    
    except MemoryError:
        print("Memória insuficiente! O programa atingiu o limite de alocação.")
        break

    time.sleep(1)