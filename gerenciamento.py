from models import GerenciamentoSaida
from typing import List
from db import get_connection

def gerar_gerenciamento(mentorado_id: str) -> List[GerenciamentoSaida]:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(""" UPDATE mentorings
                       SET concluded = true
                       WHERE TIMESTAMPDIFF(MINUTE,scheduled_date,DATE_SUB(NOW(), INTERVAL 3 HOUR)) > 0
                       AND mentored_id = %s""",(mentorado_id,))
    conn.commit()

    cursor.execute("""SELECT 
            T2.id,
            T2.name AS mentoring_name,
            T3.name AS mentor_name,
            T1.name AS mentored_name,
            T2.scheduled_date
            FROM users T1
            LEFT JOIN mentorings T2
                ON T1.id = T2.mentored_id
            LEFT JOIN users T3
                ON T2.mentor_id = T3.id
            WHERE TRUE 
            AND T2.concluded IS FALSE
            AND T1.id = %s""", (mentorado_id,))
    sugestoes = cursor.fetchall()

    cursor.close()
    conn.close()

    return [GerenciamentoSaida(
        id=sugestao['id'],
        name=sugestao['mentoring_name'],
        mentor_name=sugestao['mentor_name'],
        mentored_name=sugestao['mentored_name'],
        scheduled_date=sugestao['scheduled_date']
    ) for sugestao in sugestoes]