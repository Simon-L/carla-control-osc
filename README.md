# Carla control programmatically

Better get yourself an isolated environment! I choose virtualenv.

```
python3 -p venv .venv
source .venv/bin/activate
pip install cython
pip install pyliblo@git+https://github.com/Houston4444/pyliblo@master
```

First start carla in another terminal: `carla empty.carxp -n`.
Then `python basic_lv2_plugin.py`
