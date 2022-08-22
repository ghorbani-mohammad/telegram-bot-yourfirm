
from api.yourfirm import Yourfirm


def test_yourfirm_api():
    # in the good situation, we should get response
    # and in the response we have a result field which has
    # greater or equal to zero items
    assert len(Yourfirm.search(term='python')['result']) >= 0
