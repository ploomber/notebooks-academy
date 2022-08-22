import pytest
from ploomber_engine.ipython import PloomberClient


@pytest.fixture
def defs():
    client = PloomberClient.from_path("notebook.ipynb")
    return client.get_definitions()


def test_tags_len(defs):
    tags_len = defs["tags_len"]
    assert tags_len([1, 2, 3]) == 3


def test_parse_tags(defs):
    parse_tags = defs["parse_tags"]
    assert parse_tags([["rock", 100], ["pop", 50]]) == {
        "tag_0": "rock",
        "tag_1": "pop",
        "value_0": 100,
        "value_1": 50,
    }
