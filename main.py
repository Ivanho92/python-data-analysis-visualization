from src.crawler.index import crawl
from src.modeler.index import prepare_model
from src.visualization.index import generate_js

# 1) Crawl data and store it to db
crawl()

# 2) Prepare model and store it
prepare_model()

# 3) Generate javascript for visualization
generate_js()
