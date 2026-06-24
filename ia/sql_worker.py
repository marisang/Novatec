def gerar_sql(pergunta):

    sql = blazesql.generate(
        pergunta
    )

    return sql