
from Tests.Config.swagr_fixtures import *
from Tests.Config.Ui_fixtures import *
#c="C:\\as\\chromedriver.exe"
def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="http://localhost/")
    parser.addoption("--urlSwgr", action="store", default="http://localhost:7017/")
    parser.addoption("--drvrPath",action="store",default="C:\\as\\chromedriver.exe")
    parser.addoption("--frmwrk",action="store",default="P")
    parser.addoption("--brows",action="store",default="C")
    parser.addoption("--cmdexec",action="store",default="http://localhost:4444/wd/hub")
    parser.addoption("--CapPath", action="store", default="C:\\as\\data.json.txt")

#"C:\\as\\chromedriver.exe"

@pytest.fixture(scope="session")
def get_url(request):
    return request.config.getoption("--url")
@pytest.fixture(scope="session")
def SwgrUrl(request):
    return request.config.getoption("--urlSwgr")
@pytest.fixture(scope="session")
def getdriverPath(request):
    return request.config.getoption("--drvrPath")
@pytest.fixture(scope="session")
def getBrowser(request):
    return request.config.getoption("--brows")
@pytest.fixture(scope="session")
def getCmdExec(request):
    return request.config.getoption("--cmdexec")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

#
# f = open(filePath, "r")
#         capabilities=json.load(f)