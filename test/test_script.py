from script import main

def test_main_output(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hola" in captured.out