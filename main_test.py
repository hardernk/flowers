import main


def test_blooming_flowers():
    assert main.blooming_flowers('May') == ['peonies', 'rhododendrons',
                                            'lilac']
    assert len(main.blooming_flowers('March')) == 3

    assert main.blooming_flowers('mai') == []
    assert main.blooming_flowers('') == []
