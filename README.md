# air-teach-business-back

### создание виртуальной среды
python -m venv .venv

### запуск виртуальной среды
.venv\Scripts\Activate.ps1 

### установка зависимостей проекта
pip install -r requirements.txt

### запуск проекта в dev режиме
uvicorn app.main:app --reload