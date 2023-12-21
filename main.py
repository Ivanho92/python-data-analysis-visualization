from src.crawler.index import crawl
from src.modeler.index import prepare_model
from src.visualization.index import generate_js

# 1) Crawl data and store it to db
crawl()

# 2) Prepare model and store it also to (separate) db
prepare_model()

# 3) Generate javascript for visualization
generate_js()

print('Program finished! You can now open the app in the browser: ' +
      'http://localhost:63342/cocaine-seizures-europe/src/visualization/index.html')
