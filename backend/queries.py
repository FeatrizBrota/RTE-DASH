import connector_db as cdb

cur_dev = cdb.conexao_dev.cursor()
cur_hml = cdb.conexao_hml.cursor()
cur_prod = cdb.conexao_prod.cursor()


def q_cenarios_gerados_dev():
    query = ("SELECT"
             " DATE_FORMAT(lc.created_at,'%m/%Y') AS mes,"
             " COUNT(lc.id_log_cenario) AS total_cenario"
             " FROM log_acesso la"
             " LEFT JOIN log_cenario lc ON la.id_log_acesso = lc.id_log_acesso"
             " INNER JOIN usuario_config uc ON la.id_usuario = uc.id_usuario"
             " WHERE MONTH(lc.created_at) IN (01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12)"
             " AND YEAR(lc.created_at) = 2023"
             " AND (uc.tipo_id != 6 OR uc.tipo_id != 8)"
             " GROUP BY mes"
             " ORDER BY mes, total_cenario DESC;")
    cur_dev.execute(query)
    return cur_dev.fetchall()


def q_cenarios_gerados_prod():
    query = ("SELECT"
             " DATE_FORMAT(lc.created_at,'%m/%Y') AS mes,"
             " COUNT(lc.id_log_cenario) AS total_cenario"
             " FROM log_acesso la"
             " LEFT JOIN log_cenario lc ON la.id_log_acesso = lc.id_log_acesso"
             " INNER JOIN usuario_config uc ON la.id_usuario = uc.id_usuario"
             " WHERE MONTH(lc.created_at) IN (01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12)"
             " AND YEAR(lc.created_at) = 2023"
             " AND (uc.tipo_id = 6 OR uc.tipo_id = 8)"
             " GROUP BY mes"
             " ORDER BY mes, total_cenario DESC;")
    cur_prod.execute(query)
    return cur_prod.fetchall()


def q_total_acessos_dev():
    query = ("SELECT"
             " DATE_FORMAT(la.created_at,'%m/%Y') AS mes,"
             " COUNT(*) AS total_acessos"
             " FROM log_acesso la"
             " INNER join usuario_config uc ON la.id_usuario = uc.id_usuario"
             " WHERE MONTH(la.created_at) IN (01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12)"
             " AND YEAR(la.created_at) = 2023"
             " AND (uc.tipo_id != 6 OR uc.tipo_id != 8)"
             " GROUP BY mes"
             " ORDER BY mes, total_acessos;")
    cur_dev.execute(query)
    return cur_dev.fetchall()


def q_total_acessos_prod():
    query = ("SELECT"
             " DATE_FORMAT(la.created_at,'%m/%Y') AS mes,"
             " COUNT(*) AS total_acessos"
             " FROM log_acesso la"
             " INNER join usuario_config uc ON la.id_usuario = uc.id_usuario"
             " WHERE MONTH(la.created_at) IN (01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12)"
             " AND YEAR(la.created_at) = 2023"
             " AND (uc.tipo_id = 6 OR uc.tipo_id = 8)"
             " GROUP BY mes"
             " ORDER BY mes, total_acessos;")
    cur_prod.execute(query)
    return cur_prod.fetchall()


def q_empresas_criadas_dev():
    query = ("SELECT"
             " DATE_FORMAT(em.created_at,'%m/%Y') AS mes,"
             " COUNT(em.id) AS total"
             " FROM empresa em"
             " INNER JOIN usuario_config uc ON em.id_usuario = uc.id_usuario"
             " WHERE MONTH(em.created_at) IN (01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12) AND YEAR(em.created_at) "
             "= 2023"
             " AND (uc.tipo_id != 6 OR uc.tipo_id != 8)"
             " GROUP BY mes"
             " ORDER BY mes, total;")
    cur_dev.execute(query)
    return cur_dev.fetchall()


def q_empresas_criadas_prod():
    query = ("SELECT"
             " DATE_FORMAT(em.created_at,'%m/%Y') AS mes,"
             " COUNT(em.id) AS total"
             " FROM empresa em"
             " INNER JOIN usuario_config uc ON em.id_usuario = uc.id_usuario"
             " WHERE MONTH(em.created_at) IN (01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12) AND YEAR(em.created_at) "
             "= 2023"
             " AND (uc.tipo_id = 6 OR uc.tipo_id = 8)"
             " GROUP BY mes"
             " ORDER BY mes, total;")
    cur_prod.execute(query)
    return cur_prod.fetchall()


def total_acessos_dev():
    query = ("SELECT"
             " DATE_FORMAT(la.created_at,'%m/%Y') AS mes,"
             " COUNT(*) AS total_acessos"
             " FROM log_acesso la"
             " INNER join usuario_config uc ON la.id_usuario = uc.id_usuario"
             " WHERE MONTH(la.created_at) IN (01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12) AND YEAR(la.created_at) "
             "= 2023"
             " AND (uc.tipo_id != 6 OR uc.tipo_id != 8)"
             " GROUP BY mes"
             " ORDER BY mes, total_acessos;")
    cur_dev.execute(query)
    return cur_dev.fetchall()


def total_acessos_prod():
    query = ("SELECT"
             " DATE_FORMAT(la.created_at,'%m/%Y') AS mes,"
             " COUNT(*) AS total_acessos"
             " FROM log_acesso la"
             " INNER join usuario_config uc ON la.id_usuario = uc.id_usuario"
             " WHERE MONTH(la.created_at) IN (01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12) AND YEAR(la.created_at) "
             "= 2023"
             " AND (uc.tipo_id = 6 OR uc.tipo_id = 8)"
             " GROUP BY mes"
             " ORDER BY mes, total_acessos;")
    cur_prod.execute(query)
    return cur_prod.fetchall()


def total_monitoria_dev():
    query = ("SELECT"
             " tm.descricao AS tipo_monitoria,"
             " DATE_FORMAT(pm.created_at,'%m/%Y') AS mes,"
             " COUNT(pm.id_tipo_monitoria) AS total_monitoria"
             " FROM produto_monitoria AS pm"
             " JOIN produto AS p on pm.id_produto = p.id"
             " JOIN tipo_tributacao AS tipo_trib on pm.id_tipo_monitoria = tipo_trib.id_tipo_monitoria"
             " JOIN tipo_monitoria AS tm on tipo_trib.id_tipo_monitoria = tm.id_tipo_monitoria"
             " JOIN empresa AS e on p.id_empresa = e.id"
             " JOIN usuario_config AS uc on e.id_usuario = uc.id_usuario"
             " WHERE MONTH(pm.created_at) IN (01,02,03,04,05,06,07,08,09,10,11,12) AND YEAR(pm.created_at) = 2023"
             " AND (uc.tipo_id != 6 OR uc.tipo_id != 8)"
             " GROUP BY"
             " mes,"
             " tm.descricao")
    cur_dev.execute(query)
    return cur_dev.fetchall()


def total_monitoria_prod():
    query = ("SELECT"
             " tm.descricao AS tipo_monitoria,"
             " DATE_FORMAT(pm.created_at,'%m/%Y') AS mes,"
             " COUNT(pm.id_tipo_monitoria) AS total_monitoria"
             " FROM produto_monitoria AS pm"
             " JOIN produto AS p on pm.id_produto = p.id"
             " JOIN tipo_tributacao AS tipo_trib on pm.id_tipo_monitoria = tipo_trib.id_tipo_monitoria"
             " JOIN tipo_monitoria AS tm on tipo_trib.id_tipo_monitoria = tm.id_tipo_monitoria"
             " JOIN empresa AS e on p.id_empresa = e.id"
             " JOIN usuario_config AS uc on e.id_usuario = uc.id_usuario"
             " WHERE MONTH(pm.created_at) IN (01,02,03,04,05,06,07,08,09,10,11,12) AND YEAR(pm.created_at) = 2023"
             " AND (uc.tipo_id = 6 OR uc.tipo_id = 8)"
             " GROUP BY"
             " mes,"
             " tm.descricao")
    cur_prod.execute(query)
    return cur_prod.fetchall()
