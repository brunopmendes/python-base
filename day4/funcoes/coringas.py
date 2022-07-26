def funcao(*args, timeout=10, **kwargs): 
    """
    com *args posso passar n parametros para funcao
    com **kwargs posso passar n parametrods nomeados para funcao 
    """
    for item in args:
        print(item)
    print(kwargs)
    
    print(f"timeout {timeout}")
    
funcao("Bruno", 1, True, timeout=90, a=1, b="Teste")