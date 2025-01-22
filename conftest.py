import sys, os, json
if os.path.isdir("./.venv/lib/"):
    sys.path.append('null/site-packages')
def pytest_addoption(parser):
    parser.addoption("--stdin", action="append", default=[],
        help="json with the stdin to pass to test functions")
def pytest_generate_tests(metafunc):
    if 'stdin' in metafunc.fixturenames:
      if hasattr(metafunc,"config"):
          metafunc.parametrize("stdin",metafunc.config.getoption('stdin'))
      elif hasattr(metafunc,"configuration"):
          metafunc.parametrize("stdin",metafunc.configuration.getoption('stdin'))
      else:
          raise Exception("Imposible to retrieve text configuration object")
    if 'app' in metafunc.fixturenames:
        try:
          sys.path.append('.learn/dist')
          import cached_app
          metafunc.parametrize("app",[cached_app.execute_app])
        except SyntaxError:
          metafunc.parametrize("app",[lambda : None])
        except ImportError:
          metafunc.parametrize("app",[cached_app])
        except AttributeError:
          metafunc.parametrize("app",[cached_app])
    if 'configuration' in metafunc.fixturenames:
        metafunc.parametrize("configuration", [json.loads('{"port":3000,"os":"linux","editor":{"mode":"extension","agent":"vscode","version":"5.0"},"dirPath":"./.learn","configPath":"learn.json","outputPath":".learn/dist","publicPath":"/preview","publicUrl":"https://scaling-acorn-9wpw4979j2p47r-3000.app.github.dev","contact":"https://github.com/learnpack/learnpack/issues/new","language":"auto","autoPlay":true,"projectType":"tutorial","grading":"isolated","exercisesPath":"./exercises","webpackTemplate":null,"disableGrading":false,"disabledActions":[],"actions":[],"entries":{"html":"index.html","vanillajs":"index.js","react":"app.jsx","node":"app.js","python3":"app.py","java":"app.java"},"suggestions":{"agent":"vscode"},"warnings":{"agent":null},"title":{"en":"Learn Object Oriented Programming with Python","es":"Aprende Programación Orientada a Objetos con Python"},"slug":"python-oop-tutorial","repository":"https://github.com/4GeeksAcademy/python-oop-tutorial","preview":"https://github.com/4GeeksAcademy/python-oop-tutorial/blob/main/preview.gif?raw=true","description":{"en":"Learn Object Oriented Programming concepts using Python, from basic to advanced topics","es":"Aprende conceptos de Programación Orientada a Objetos usando Python, desde temas básicos hasta avanzados"},"duration":6,"difficulty":"easy","videoSolutions":false,"bugsLink":"https://github.com/learnpack/learnpack/issues/new","graded":true,"config":{"editor":{"version":"1.0.73"}},"translations":[]}')])
