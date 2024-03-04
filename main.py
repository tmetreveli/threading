import json
import time
from utils import CustomThread, get_data


start = time.perf_counter()
url = "https://dummyjson.com/products/"

threads = []

for product_id in range(1,101):
    t = CustomThread(target=get_data, args=(product_id,url))
    threads.append(t)
    t.start()

for thread in threads:
    result = thread.join()

    with open("sample.json", "a") as outfile:
        json.dump(result, outfile, indent=2)

end = time.perf_counter()

print(f"All the data is loaded in {end - start} time")