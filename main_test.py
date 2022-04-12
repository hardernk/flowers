import main


def test_blooming_flowers():
    assert main.blooming_flowers('may') == ['peonies', 'rhododendrons',
                                            'lilac']
    assert len(main.blooming_flowers('march')) == 3

    assert main.blooming_flowers('mai') == []
    assert main.blooming_flowers('') == []
