from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(34, 34) == TypeError("tipo inválido para message")
        encrypt_message('lrd', 'lad') == TypeError("tipo inválido para key")

    assert encrypt_message('timberlake', 5) == "ebmit_ekalr"
    assert encrypt_message('timberlake', 4) == "ekalre_bmit"
    assert encrypt_message('lazer', 7) == "rezal"
