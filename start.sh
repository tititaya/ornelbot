
#!/bin/bash
export PORT=${PORT:-10000}
streamlit run app.py --server.port=$PORT --server.enableCORS=false
