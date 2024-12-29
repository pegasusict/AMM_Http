__version__ = "0.0.1"
__build_date__ = 20241229

from AMM_HTTP import app

if __name__ == "__main__":
    app.run(debug=True)