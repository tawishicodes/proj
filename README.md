# Six Social

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/testaccount440/six
cd six
```

2. Install requirements:
- you can skip this command on windows:
```bash
python3 -m venv venv
source venv/bin/activate
```
then:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file and add your Supabase credentials: 
```
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
PORT=8000
```

4. Run the application:
```bash
python run.py
```

The server will automatically use:
- Gunicorn on Linux/macOS
- Waitress on Windows

Visit `http://localhost:8000` in your browser.
