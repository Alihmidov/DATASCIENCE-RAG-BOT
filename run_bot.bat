@echo off
echo Starting the project...
:: Open the Streamlit URL in the default browser automatically
start "" http://localhost:8501
:: Activate the virtual environment
call .\.venv\Scripts\activate
:: Start the FastAPI backend server in a new window
start python -m uvicorn app.main:app
:: Run the Streamlit UI in the current window
python -m streamlit run app/ui.py
pause