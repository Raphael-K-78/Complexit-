def fmt_time(t, enabled):
    """
    Docstring for fmt
    
    :param t: Description
    :param enabled: Description
    formater ou écrire un tiret selon si le tri a été effectué
    :return: resultat formaté
    """
    return f"{t:.6f}s" if enabled else "—"
